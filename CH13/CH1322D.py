#使用pack()方法，參數expand
from tkinter import *
root = Tk()
# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色

lbla = Label(root, text = 'Red', bg = 'red',
        fg = 'white').pack(side = 'left', expand = 1)#加入版面

lblb = Label(root, text = 'Green',
        bg = 'green', fg = 'white').pack()

lblc = Label(root, text = 'Blue',
        bg = 'blue', fg = 'white').pack()
mainloop()
