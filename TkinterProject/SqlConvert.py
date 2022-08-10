import re
from datetime import datetime
# import pyodbc

tempColumnString = '''
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'{CName}',
@level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'{TableName}', 
@level2type=N'COLUMN',@level2name=N'{ColumnName}';
GO
'''

tempTableString = '''
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'{CName}', 
@level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'{TableName}'
GO
'''


# CName = '分公司別'
# TableName = 'HSCB'
# ColumnName = 'BKNO'

tempCreateTableString = '''
CREATE TABLE "dbo".{} 
(
{}
);
'''
TableInsertString = "Insert into {DBName}.dbo.{TableName} {ColumnName} values {ColumnValues};"





# version 3
def TableAnalysis(SqlContext):
    if SqlContext == '':
        return ''
    SqlText = SqlContext
    result = re.search("CREATE TABLE (.*) SEGMENT CREATION IMMEDIATE",SqlText, flags=re.DOTALL+re.MULTILINE)
    if result == None:
        assert('error')
        return ''

    temp_table = result.group(0)
    # print(temp_table)
    table_column = re.sub("SUPPLEMENTAL LOG .*\n", '', result.group(0).replace(" (\t",'').replace(" ) SEGMENT CREATION IMMEDIATE",''))
    table_column = table_column.replace(' TIMESTAMP ',' datetime2').replace('SYSTIMESTAMP',"getdate()")
    table_column = table_column.replace("ENABLE",'').replace(" BYTE",'')
    table_column = table_column.replace('VARCHAR2','VARCHAR')
    table_column = table_column.replace('NVARCHAR2','NVARCHAR')

    tableName = table_column.split("\n")[0].split(".")[1]
    #print(tableName)


    ColumnList = []
    # 第一個是 Table
    for _ in table_column.split("\n")[1:]:
        #print("--")
        if _.strip().find("NUMBER") > -1 :
            # Number Convert
            tempNumberFormat = _.strip().replace("NUMBER(",'').replace(")",'').split(" ")
            #                 print(tempNumberFormat)
            IntOrDem = tempNumberFormat[1].split(",")
            if IntOrDem[1] == '0':
                # 'Int Kind'
                if int(IntOrDem[0]) < 4:
                    tempNumberFormat[1]='SMALLINT'
                elif int(IntOrDem[0]) < 8:
                    tempNumberFormat[1]='INT'
                else:
                    tempNumberFormat[1]='BIGINT'
                temp_string = " ".join(tempNumberFormat)
                pass
            else:
                # 'Dec kind'
                temp_string = temp_string.replace("NUMBER",'DECIMAL')
                pass
            ColumnList.append(temp_string)
            pass
        else:
            # Not Number
            if len(_.strip()) > 0 :
                ColumnList.append(_.strip())
            pass

    result = ''
    result = re.search(" CONSTRAINT (.*) PRIMARY KEY (.*) USING INDEX",SqlText, flags=re.DOTALL+re.MULTILINE)
    if result == None :
        assert('error')
        return ''

    PrimaryKey = 'CONSTRAINT {} PRIMARY KEY {}'.format(result.group(1),result.group(2))
    ColumnList.append(PrimaryKey)


    TableState = tempCreateTableString.format(tableName,"\n".join(ColumnList))
    return TableState


def COMMENTAnalysis(SqlContext):
    if SqlContext == '':
        return ''
    #     SqlContext = SqlText
    context = SqlContext.split('\n')
    commentList = []
    for _ in context:

        if _.find('COMMENT ON') <0 :
            continue
        else:
            #             print(_)

            commentType = ''
            parse_string = re.search("COMMENT ON (.*) (.*)\.(.*)\.(.*) IS (.*);", _, re.I|re.M)
            if parse_string != None:
                #                 print("-->")
                #                 print(parse_string.groups())
                #                 print(parse_string.group(1))
                commentType = 'COLUMN'
            else:

                parse_string = re.search("COMMENT ON (.*) (.*)\.(.*)  IS (.*);", _, re.I|re.M)
                if parse_string != None:
                    #                     print(parse_string.groups())
                    commentType = 'TABLE'

            if commentType == 'COLUMN':

                CName = parse_string.group(5).replace("\'",'')
                TableName = parse_string.group(3).replace("\"",'')
                ColumnName = parse_string.group(4).replace("\"",'')

                commentList.append(tempColumnString.format(CName=CName ,TableName=TableName, ColumnName=ColumnName))
                pass

            if commentType == 'TABLE':

                CName = parse_string.group(4).replace("\'",'')
                TableName = parse_string.group(3).replace("\"",'')

                commentList.append(tempTableString.format(CName=CName ,TableName=TableName))

                pass
            pass
        pass
    return "".join(commentList)


def InserDataAnalysis(DataContext,DBName= 'jsdata2',DatatimeType=2):

    InsertData = DataContext.split('\n')

    InsertList=[]
    for _ in InsertData:
        result = re.search("Insert into (.*) (.*) values (.*);",_, re.I|re.M)
        if result == None :
            continue
        #         print(_)
        #         print(result.groups())
        TableName = result.group(1)

        ColumnName = result.group(2).replace("TRAN","[TRAN]")

        temp_values = result.group(3).split(',')
        valuesList = []
        for item in temp_values:
            #             print(item)
            if item.find('to_timestamp') > -1:
                date_format = item.replace('to_timestamp(','').replace('月','').replace('下午','PM').replace('上午','AM').replace('\'','')
                #                 print(date_format)
                try:
                    date_item,time_item,type_item = date_format.split(' ')
                except:
                    date_item,time_item,type_item = date_format.replace(' -','-').split(' ')

                adj_date_format= " ".join([date_item,time_item[0:-3],type_item])
                #                 print(adj_date_format)
                # for datatime2 型態
                if DatatimeType == 2:
                    date_object = datetime.strptime(adj_date_format, "%d-%m-%y %I.%M.%S.%f %p").strftime("%Y-%m-%d %H:%M:%S.%f")
                # for  資料庫欄位型態 datatime 非 datatime2 型態
                if DatatimeType == 1:
                    date_object = datetime.strptime(adj_date_format, "%d-%m-%y %I.%M.%S.%f %p").strftime("%Y-%m-%d %H:%M:%S")
                #                 print(date_object)
                valuesList.append("\'{}\'".format(date_object))
                continue

            if item.find('DD-MON-RR') > -1:
                #                 print('==>')
                #                 print(item)
                continue

            valuesList.append(item)

        ColumnValues = ",".join(valuesList)
        temp = TableInsertString.format(DBName=DBName,TableName=TableName,ColumnName=ColumnName,ColumnValues=ColumnValues)
        InsertList.append(temp)
        pass


    return "\n".join(InsertList)
