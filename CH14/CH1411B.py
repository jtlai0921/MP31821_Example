from tkinter import *

root = Tk().withdraw() # 隱藏主視窗物件
var = messagebox.askyesno('Create File', '是否要寫入檔案')
filename = 'demo1402.txt'
with open(filename, 'w') as fin:
    fin.write(str(var))
    print(str(var) + ' File Name: ' + filename)
    
