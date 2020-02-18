#使用 Radiobutton
from tkinter import *
wnd = Tk()
wnd.title('Radiobutton')

def myOptions():
    print('Your choice is :', var.get())

ft = ('Franklin Gothic Book', 14)
Label(wnd, 
      text = """ 選擇你 - 
最愛的水果：""", font = ft,
      justify = LEFT, padx = 20).pack()

fruits = [('Watermelon', 1), ('Pompelmous', 2),
          ('Strawberry', 3), ('Orange', 4),
          ('Apple', 5), ('Dragon fruit', 6)]
var = IntVar()
var.set(3)
for item, val in fruits:    
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 15,
        command = myOptions).pack(anchor = W)
    '''
    Radiobutton(wnd, text = item, indicatoron = 0,
                width = 20, padx = 25, 
                variable = var, 
                command = myOptions,
                value = val).pack(anchor=W)'''
mainloop()


