# Button的屬性state
from tkinter import *
wnd = Tk()
wnd.title('Button state...')

#屬性state的參數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = Button(wnd, text = item, state = item)
    btn.pack()

wnd.mainloop()
