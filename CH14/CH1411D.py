# messagebox回應訊息

from tkinter import *

wnd = Tk()
wnd.title('Messagebox')
wnd.geometry('180x120+20+50')

def answer(): #回應 Answer 按鈕
    messagebox.showerror('Answer',
            '抱歉！, 你的問題無法回答')

def callback():
    if messagebox.askyesno('訊息確認',
            '真得要離開嗎？'):
        messagebox.showwarning('訊息 - Yes',
            '抱歉!無法離開')
    else:
        messagebox.showinfo(
            '訊息 - No', '取消「離開」指令')

Button(wnd, text='Quit', command =
       callback).pack(side = 'left', padx = 10)
Button(wnd, text='Answer', command =
       answer).pack(side = 'left')
mainloop()
