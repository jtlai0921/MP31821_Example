# 以place()方法，以座標做元件的版面管理
from tkinter import *
import random

wnd = Tk() #建立主視窗物件

# width x height + x_offset + y_offset:
wnd.geometry('180x200+40+40') #設定版面寬度
     
names = ['Peter','Vicky','Michelle','Joson','Tomas']
peop = range(5)
for item in range(5):
   ct = [random.randrange(256) for x in range(3)]
   tint = int(round(0.2*ct[0] + 0.5*ct[1] + 0.1*ct[2]))
   #將顏色轉為16進位來呈現
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   lbl = Label(wnd, text = names[item], bg = bg_colour,
               fg = 'white' if tint < 120 else 'black')
   lbl.place(x = 20, y = 30 + item*30,
        width = 140, height = 28)
          
wnd.mainloop()
