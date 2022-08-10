# 參考
# Python tkinter filedialog 開啟檔案對話框
# https://shengyu7697.github.io/python-tkinter-filedialog/
# https://blog.csdn.net/weixin_44630029/article/details/104399156
#
# openfiledialog - Quick and easy file dialog in Python? - Stack Overflow
# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
# Tkinter Dialogs — Python 3 documentation
# https://docs.python.org/3/library/dialog.html
# Tkinter tkFileDialog module - Python Tutorial
# https://pythonspot.com/tk-file-dialogs/

import tkinter as tk

from tkinter import filedialog


root = tk.Tk()

# Hide the main window
root.withdraw()
#
#file_path = filedialog.askopenfilename(parent=root,title='Select file',initialdir=r'~\Downloads')
# 沒有 root 還是可以開啟 對話窗
file_path = filedialog.askopenfilename(title='Select file',initialdir=r'~\Downloads')
#  file dialog 選取檔案並按下開啟按鈕後，才會有回傳值(檔案路徑)
#  回傳的類型為 str，若取消的話會回傳一個空的 tuple ()
#  title 參數: 為設定對話框的標題
#  initialdir='~/' 參數: 初始的目錄來開啟檔案設定
print(type(file_path))

if not file_path:
    print('file path is empty')
else:
    with open(file_path, 'r') as f:
        print(f.read())


#如果要使視窗再次可見，請呼叫deiconify(或wm_deiconify)方法。
root.deiconify()

root.mainloop()