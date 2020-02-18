from tkinter import *

''' 以place()方法，將兩個Frame 進行版面配置
    relief: FLAT, SUNKEN, RAISED, GROOVE, and RIDGE
'''

wnd = Tk()#建立主視窗物件

#產生兩個Frame，呼叫place()方法，透過split值做水平分割
f1 = Frame(wnd, bd = 1, relief = 'ridge')
f2 = Frame(wnd, bd = 1, relief = 'flat')

split = 0.3 #分割值
f1.place(rely = 0, relwidth = 1, relheight = split)
f2.place(rely = split, relwidth = 1,
         relheight = 1 - split)
