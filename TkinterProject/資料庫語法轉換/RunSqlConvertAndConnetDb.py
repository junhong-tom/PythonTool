import tkinter as tk
from  tkinter import Button, StringVar, Label ,LEFT,W,WORD ,Text,END,Scrollbar,HORIZONTAL,RIGHT,Entry
from tkinter import filedialog, messagebox, Checkbutton, IntVar
from tkinter.scrolledtext import ScrolledText
from configFile import GetInitConfig

from SqlConvert import  TableAnalysis , COMMENTAnalysis ,InserDataAnalysis, SqlCommand,InsertMutilData


def SaveTableSchema():
    contex_text = Text_001.get("1.0","end")

    saveFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if saveFile == None:
        #root.deiconify()

        pass
    else:
        saveFile.write(contex_text)

        saveFile.close()
    return

def ConverTableSchema():
    global  FilePath
    FilePath = ''
    Text_001.delete("1.0","end")
    #root.withdraw()
    #
    #file_path = filedialog.askopenfilename(parent=root,title='Select file',initialdir=r'~\Downloads')
    # 沒有 root 還是可以開啟 對話窗
    file_path = filedialog.askopenfilename(title='Select file',initialdir=r'~\Downloads')
    #  file dialog 選取檔案並按下開啟按鈕後，才會有回傳值(檔案路徑)
    #  回傳的類型為 str，若取消的話會回傳一個空的 tuple ()
    #  title 參數: 為設定對話框的標題
    #  initialdir='~/' 參數: 初始的目錄來開啟檔案設定
    print(file_path)

    if not file_path:
        print('file path is empty')
        # varTableContext.set('')
        # varCommentContext.set('')
    else:
        with open(file_path, 'r') as f:
            SqlContext = f.read()
    if not file_path :
        pass
    else:
        ConvertContext = TableAnalysis(SqlContext)


        COMMENTContext = COMMENTAnalysis(SqlContext)
        Text_001.insert(END, ConvertContext+'\n'+COMMENTContext)
        # Text_001.config(text=ConvertContext+'\n'+COMMENTContext)
        #varCommentContext.set(COMMENTContext)


    return

def ConverInsertDataSchema():
    Text_001.delete("1.0","end")
    #root.withdraw()
    global FilePath

    #file_path = filedialog.askopenfilename(parent=root,title='Select file',initialdir=r'~\Downloads')
    # 沒有 root 還是可以開啟 對話窗
    FilePath = filedialog.askopenfilename(title='Select file',initialdir=r'~\Downloads')
    #  file dialog 選取檔案並按下開啟按鈕後，才會有回傳值(檔案路徑)
    #  回傳的類型為 str，若取消的話會回傳一個空的 tuple ()
    #  title 參數: 為設定對話框的標題
    #  initialdir='~/' 參數: 初始的目錄來開啟檔案設定
    #print(file_path)

    if not FilePath:
        print('file path is empty')

    else:
        with open(FilePath, 'r') as f:
            SqlContext = f.read()
    print('--->')
    print(InserMutilValues.get())
    if not FilePath :
        pass
    else:
        DBName = DataBaseNameEntry.get()
        if DBName != '':
            if InserMutilValues.get() != 0 :
                InsertContext = InsertMutilData(SqlContext,DBName)
            else:
                InsertContext = InserDataAnalysis(SqlContext,DBName)
        else:
            if InserMutilValues.get() != 0 :
                InsertContext = InsertMutilData(SqlContext,'CFP')
            else:
                InsertContext = InserDataAnalysis(SqlContext,'CFP')

        Text_001.insert(END, InsertContext)
    return

def RunSqlCommand():
    ServerIP = ServerIPEntry.get()
    DBName = DataBaseNameEntry.get()
    User = UserEntry.get()
    PWD = PWDEntry.get()
    contex_text = Text_001.get("1.0","end")
    EnabledCommand = True

    if (ServerIP == '') or (DBName == '') or (User == '') or (PWD == '') or ( contex_text == '') :

        EnabledCommand = False
        messagebox.showinfo('訊息錯誤', '請確認相關輸入的訊息')
        pass





    if EnabledCommand :
        try:
            Res = SqlCommand(ServerIP,DBName,User,PWD,contex_text)
            messagebox.showinfo('指令完成:', Res)
        except Exception as commandError:
            # print('----->>')
            # print(commandError)
            messagebox.showinfo('資料庫錯誤', str(commandError))
    # print('IP:'+ServerIP+',db:'+DBName+',user:'+User+',pwd:'+PWD)

    return

def InitFunction():

    try:
        ServerIP,DBName,User,PWD =  GetInitConfig()
    except Exception as configError:
        print(configError)
        ServerIP = ''
        DBName = ''
        User = ''
        PWD = ''

    PWDEntry.insert(0,PWD)
    UserEntry.insert(0,User)
    DataBaseNameEntry.insert(0,DBName)
    ServerIPEntry.insert(0,ServerIP)
    return


FilePath = ''
root = tk.Tk()
root.resizable(0,0)
root.title("ConvertSqlSchema")
root.geometry("600x600")


ConverTableSchemaButton = Button(text='資料表轉換',command=ConverTableSchema,width=14,bg="red",font="微軟正黑 +12")
ConverTableSchemaButton.grid(row=0,column=0,padx=5,pady=1)

SaveTableSchemaButton = Button(text='資料表存檔',command=SaveTableSchema,width=14,bg="skyblue",font="微軟正黑 +12")
SaveTableSchemaButton.grid(row=0,column=1,padx=5,pady=1)
# Label('').grid(row=0,column=2)

ConverInsertDataSchemaButton = Button(text='匯入資料轉換',command=ConverInsertDataSchema,width=14,bg="red",font="微軟正黑 +12")
ConverInsertDataSchemaButton.grid(row=1,column=0,padx=5,pady=1)
SaveTableSchemaButton = Button(text='匯入資料存檔',command=SaveTableSchema,width=14,bg="skyblue",font="微軟正黑 +12")
SaveTableSchemaButton.grid(row=1,column=1,padx=5,pady=1)
# Label('').grid(row=1,column=2)

def ChangeValuesType():


    print("Change: "+FilePath)
    if FilePath == '':
        return
    Text_001.delete("1.0","end")

    with open(FilePath, 'r') as f:
        SqlContext = f.read()

    DBName = DataBaseNameEntry.get()
    if DBName != '':
        if InserMutilValues.get() != 0 :
            InsertContext = InsertMutilData(SqlContext,DBName)
        else:
            InsertContext = InserDataAnalysis(SqlContext,DBName)
    else:
        if InserMutilValues.get() != 0 :
            InsertContext = InsertMutilData(SqlContext,'CFP')
        else:
            InsertContext = InserDataAnalysis(SqlContext,'CFP')

    Text_001.insert(END, InsertContext)



    return

InserMutilValues = IntVar()
Checkbutton( text="多值輸入", variable=InserMutilValues,command = ChangeValuesType,font="微軟正黑 +12").grid(row=0,column=3, sticky=W)












RunSqlStatementsButton = Button(text='執行SQL語法',command=RunSqlCommand,width=14,bg="Green",font="微軟正黑 +12")
RunSqlStatementsButton.grid(row=1,column=3,padx=5,pady=1)



ServerIPLabel = Label(text='主機位置 IP:',font="微軟正黑 +12")
ServerIPLabel.grid(row=2,column=0,padx=5,pady=1)
ServerIPEntry = Entry(width=14,font="微軟正黑 +12")
ServerIPEntry.grid(row=2,column=1,padx=5,pady=1)

DataBaseNameLabel = Label(text='資料庫名稱:',font="微軟正黑 +12")
DataBaseNameLabel.grid(row=2,column=2,padx=5,pady=1)
DataBaseNameEntry = Entry(width=14,font="微軟正黑 +12")
DataBaseNameEntry.grid(row=2,column=3,padx=5,pady=1)

UserLabel = Label(text='使用者:',font="微軟正黑 +12")
UserLabel.grid(row=3,column=0,padx=5,pady=1)
UserEntry = Entry(width=14,font="微軟正黑 +12")
UserEntry.grid(row=3,column=1,padx=5,pady=1)

PWDLabel = Label(text='密碼:',font="微軟正黑 +12")
PWDLabel.grid(row=3,column=2,padx=5,pady=1)
PWDEntry = Entry(width=14,font="微軟正黑 +12")
PWDEntry.grid(row=3,column=3,padx=5,pady=1)




Text_001= ScrolledText(root,wrap=tk.WORD,font="微軟正黑 +12")
Text_001.config(wrap=tk.WORD,font="微軟正黑 +12")
Text_001.place(x=10,y=120,width=550,height=500)

InitFunction()

# # text_v = "Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming."
# # text_h = ("\nNASA \n Google \nNokia \nFacebook \n Netflix \n Expedia \n Reddit \n Quora \n MIT\n Udemy \n Shutterstock \nSpotify\nAmazon\nMozilla\nDropbox")
#
# #Add a Vertical Scrollbar
# scroll_v = Scrollbar(root)
# #scroll_v.pack(side= RIGHT,fill="y")
# scroll_v.place(relheight=1)
#
# #Add a Horizontal Scrollbar
# scroll_h = Scrollbar(root, orient= HORIZONTAL)
# scroll_h.place(relwidth=1)
# #scroll_h.pack(side= BOTTOM, fill= "x")
# #Add a Text widget
# Text_001 = Text(root, height= 500, width= 350, yscrollcommand= scroll_v.set,
#             xscrollcommand = scroll_h.set, wrap= tk.WORD, font= ('Helvetica 12'))
# # Text_001 = Text(root, height= 500, width= 350, yscrollcommand= scroll_v.set,
# #                 xscrollcommand = scroll_h.set, wrap= None, font= ('Helvetica 12'))
# #Text_001.pack(fill = BOTH, expand=0)
# Text_001.place(x=20,y=60,width=500,height=300)
# # Text_001.insert(END, text_v)
# # Text_001.insert(END, text_h)
#
# #Attact the scrollbar with the text widget
# scroll_h.config(command = Text_001.xview)
# scroll_v.config(command = Text_001.yview)
#


# scr = scrolledtext.ScrolledText(self.monty, width=30, height=3, wrap=tk.WORD)
# scr.grid(column=0, row=3, sticky='WE', columnspan=3)










# def file_save():
#     f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
#     if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
#         return
#     text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
#     f.write(text2save)
#     f.close() # `()` was missing.

#如果要使視窗再次可見，請呼叫deiconify(或wm_deiconify)方法。




#root.deiconify()
root.mainloop()