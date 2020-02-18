from tkinter import *

wnd = Tk()
gs = Canvas(wnd, width = 190, height = 150)
gs.pack()

#繪製橢圓形
gs.create_oval(30, 50, 170, 120, fill = 'sky blue',
    outline = 'red')

#繪製文字
gs.create_text(80, 20, text = '繪製橢圓',
    fill = 'dark red', font = ('標楷體', 26))
mainloop()
