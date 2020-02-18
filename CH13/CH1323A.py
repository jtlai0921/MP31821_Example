from tkinter import *
# 以grid()方法，將4個元件以列、欄做版面配置

wnd = Tk()
wnd.title('grid()方法')

#標籤：
Label(wnd, text = 'First').grid(row = 0, sticky = 'w')
Label(wnd, text = 'Second').grid(row = 1, sticky = 'w')

#單行文字方法
e1 = Entry(wnd)
e2 = Entry(wnd)
e1.grid(row = 0, column =1)
e2.grid(row = 1, column =1)
   
