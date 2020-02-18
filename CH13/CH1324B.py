from tkinter import *
wnd = Tk() #建立主視窗物件
wnd.title('place()方法')
#標籤 - bg 設背景色
t1 = Label(wnd, text = 'First', bg = 'white',)
t2 = Label(wnd, text = 'Second', bg = 'pink',)

# 呼叫()方法，相對於視窗X座標(0.2)
t1.place(relx = 0.2, x = 0, y = 0,
         width = 120, height = 28)
t2.place(relx = 0.2, x = 1, y = 30,
         width = 120, height = 28)
