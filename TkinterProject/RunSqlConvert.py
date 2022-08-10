import tkinter as tk
from  tkinter import Button, StringVar, Label ,LEFT,W,WORD ,Text,END
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

from SqlConvert import  TableAnalysis , COMMENTAnalysis ,InserDataAnalysis


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

    else:
        with open(file_path, 'r') as f:
            SqlContext = f.read()
    if not file_path :
        pass
    else:

        InsertContext = InserDataAnalysis(SqlContext,DBName='',DatatimeType=2)

        Text_001.insert(END, InsertContext)



    return


root = tk.Tk()
root.title("ConvertSqlSchema")
root.geometry("1100x500")


ConverTableSchemaButton = Button(text='資料表轉換',command=ConverTableSchema)
ConverTableSchemaButton.grid(row=0,column=0)

SaveTableSchemaButton = Button(text='資料表存檔',command=SaveTableSchema)
SaveTableSchemaButton.grid(row=0,column=1)
# Label('').grid(row=0,column=2)

ConverInsertDataSchemaButton = Button(text='匯入資料轉換',command=ConverInsertDataSchema)
ConverInsertDataSchemaButton.grid(row=1,column=0)
SaveTableSchemaButton = Button(text='匯入資料存檔',command=SaveTableSchema)
SaveTableSchemaButton.grid(row=1,column=1)
# Label('').grid(row=1,column=2)


Text_001= ScrolledText(root,width=120,wrap=tk.WORD,font="微軟正黑 +12")
#Text_001.grid(row=2,column=0,fill=tk.BOTH, side=tk.LEFT, expand=True)
#Text_001.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
Text_001.grid(row=2,column=0,columnspan=5,sticky='nesw', padx=3, pady=3,)
#Text_001.config(fill=tk.BOTH,side=tk.LEFT,expand=True)
# Text_001= Text( wrap=WORD)
# Text_001.grid(row=2,column=0,columnspan=3)


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