#使用pack()方法，參數side
from tkinter import *
root = Tk()
# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(root, text = 'Red', bg = 'red',
        fg = 'white').pack(side = 'right')#加入版面
lblb = Label(root, text = 'Green',
        bg = 'green', fg = 'white').pack(
        side = 'right', padx = 5, pady = 10)
lblc = Label(root, text = 'Blue',
        bg = 'blue', fg = 'white').pack(side = 'right')
mainloop()
