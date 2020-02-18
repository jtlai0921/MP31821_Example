#使用Entry來接收文字
from tkinter import *

wnd = Tk()

e = Entry(wnd, show = '*', font = ('Arial', 16))
e.grid(row = 0, column = 1)

lbl = Label(wnd, text = 'Password: ',
    height = 4).grid(row = 0, column = 0)

e.focus_set()#取得輸入焦點

def callback():#取得Button的Command訊息
    print('Your password:', e.get())
    
btn = Button(wnd, text = 'Send', width = 8,
    command = callback)

btn.grid(column = 1)





