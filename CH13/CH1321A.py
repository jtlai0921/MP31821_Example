from tkinter import *
class appWork(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
#產生物件
work = appWork()
# 顯示於視窗標題列
work.master.title('Python GUI')
work.master.maxsize(1000, 400)
# 視窗訊息初始化
work.mainloop()

