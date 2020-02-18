from tkinter import *

wnd = Tk()
wnd.title('簡單的滑鼠事件')

def callback(event):
    print('按一下滑鼠，座標：', event.x, event.y)
    
frame = Frame(wnd, width = 100, height = 100)
#按一下滑鼠的左鍵
frame.bind('<Button-1>', callback)
frame.pack()

wnd.mainloop()
