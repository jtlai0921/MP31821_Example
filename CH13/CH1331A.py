#Lable的使用
from tkinter import *

wnd = Tk() #建立主視窗物件
wnd.title('使用Label')
photo = PhotoImage(file = '03.png')#建立圖片

#標籤 - bg 設背景色
t1 = Label(wnd, text = 'Hello\n Python', bg = '#78A', 
    fg = '#FF0', relief = 'groove', bd = 2, 
    width = 15, height = 3, justify = 'right')

t2 = Label(wnd, text = '世界', width = 6, height = 4,
    relief = RIDGE, bg = 'pink', font = ('標楷體', 16))

t3 = Label(wnd, image = photo, relief = 'sunken',
    bd = 5, width = 150, height = 120)

t1.grid(row = 0, column = 0)
t2.grid(row = 0, column = 1)
t3.grid(columnspan = 2)
