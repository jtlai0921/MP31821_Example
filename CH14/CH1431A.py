# Canvas元件繪製圖形
from tkinter import *
wnd = Tk()
wnd.title('Canvas繪圖')
photo = PhotoImage(file = '03.png')
gs = Canvas(wnd)
#載入圖片
gs.create_image(80, 120, image = photo)
gs.pack()
