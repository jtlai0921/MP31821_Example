#以geometry()方法設定主視窗物件的大小
from tkinter import *
wnd = Tk()
wnd.title('Main Window')
wnd.geometry('220x150+5+40')
little = Label(wnd, text = 'Label: First',
        bg = 'skyblue').pack()
bigger = Label(wnd, text ='Label: Second',
        bg = 'pink').pack()
wnd.mainloop()

