#在視窗底部產生狀態列

from tkinter import *

class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd = 1, bg = 'sky blue',
            relief = SUNKEN, anchor = W)
        self.label.pack(fill = X)
    def set(self, format, *args):
        self.label.config(text = format % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text = '')
        self.label.update_idletasks()
root = Tk()
root.title('Contextual Menus')
root.geometry('150x120')
status = StatusBar(root)
status.pack(side = BOTTOM, fill = X, )

Label(text = 'Open:').pack(side = 'left')
Entry().pack(side = 'left')
Button(text = 'Quit', command = root.destroy).pack()
mainloop()
