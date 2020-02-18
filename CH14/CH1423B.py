# 回傳按鍵值
from tkinter import *
root = Tk()
root.title('Event Key')
root.geometry('150x50')

def showHelp(event):
    print(event.keysym, 'is Help:')
    
def sayKey(event):
    print('按鍵：{}, 字元：{}'.format(
        event.keysym, event.char))
    
frm = Frame(root, takefocus = 1,
    highlightthickness = 2)
text = Entry(frm, width = 12, takefocus = 1)

root.bind_all('<F1>', showHelp)
text.bind_class('Entry', '<Key>',
    lambda e, x = 101: sayKey(e))
root.bind('<Alt-KeyPress>', sayKey)
frm.bind('<Control-Shift-Down>' , sayKey)

text.pack()
frm.pack(side = 'bottom')
text.focus_set()
root.mainloop()

