# 一個簡單的視窗程式
from tkinter import Tk, Frame, Button
from datetime import date

class wndApp(Frame):
    def __init__(self, ruler = None):
        Frame.__init__(self, ruler)
        self.pack()
        self.makeComponent()

    def makeComponent(self): # 建立兩個按鈕
        #位於Frame左側按鈕
        self.day_is = Button(self)
        # text - 在按鈕上顯示文字
        self.day_is['text'] = '我是 按鈕\n(Click Me ...)'
        #command會去呼叫dislply()方法做回應 -- 按一下滑鼠顯示訊息
        self.day_is['command'] = self.display
        self.day_is.pack(side = 'left')
        #位於Frame右側按鈕 - command呼叫destroy()方法來清除主視窗物件
        self.QUIT = Button(self, text = 'QUIT',
                fg = 'blue', command = wnd.destroy)
        self.QUIT.pack(side = 'right')

    def display(self):
        today = date.today()
        print('Day is', today)

wnd = Tk()#產生主視窗物件
work = wndApp(ruler = wnd)
work.mainloop()#訊息呼叫


