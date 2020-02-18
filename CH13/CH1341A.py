#使用Checkbutton - 多選鈕

from tkinter import *
wnd = Tk()
wnd.title('Checkbutton')

def varStates(): #回應核取方塊變數狀態
   print('興趣，有:', var1.get(), var2.get(),
        var3.get())
   
ft1 =('微軟正黑體', 14)
ft2 = ('Levenim MT', 16)
lbl = Label(wnd, text = '興趣：', font = ft1)
lbl.grid(row = 0, column = 0)

item1 = '音樂'
var1 = StringVar()
chk = Checkbutton(wnd, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk.grid(row = 0, column = 1)

item2 = '閱讀'
var2 = StringVar()
chk2 = Checkbutton(wnd, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.grid(row = 0, column = 2)

item3 = '爬山'
var3 = StringVar()
chk3 = Checkbutton(wnd, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.grid(row = 0, column = 3)

btnQuit = Button(wnd, text = 'Quit', font = ft2, command = wnd.destroy)
btnQuit.grid(row = 2, column = 1, pady = 4)

btnShow = Button(wnd, text = 'Show', font = ft2, command = varStates)
btnShow.grid(row = 2, column = 2, pady = 4)

mainloop()
