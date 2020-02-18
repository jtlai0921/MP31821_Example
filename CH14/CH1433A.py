from tkinter import *

wnd = Tk()
wnd.title('繪製 線條、矩形')
gs = Canvas(wnd, width = 200, height = 110)
gs.pack()
gs.create_rectangle(
    50, 20, 150, 80, fill = '#00CCFF')
gs.create_rectangle(
    65, 35, 135, 65, fill= '#FF00FF')

#左上角
gs.create_line(0, 0, 50, 20,
    fill = '#0E6042', width = 5)
#左下角
gs.create_line(0, 110, 50, 80,
    fill = '#4FE222', width = 4)
#右上角
gs.create_line(150, 20, 200, 0,
    fill = '#476042', width = 3)
#右下角
gs.create_line(150, 80, 200, 110,
    fill = '#0CF042', width = 6)

mainloop()
