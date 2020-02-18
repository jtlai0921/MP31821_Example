#使用Frame - relief屬性來顯示框線
from tkinter import *

#relief常數值以list物件儲存
easyup = [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]

class appWork(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        for item in easyup: #讀取relief常數值            
            fm = Frame(master, borderwidth = 2,
                relief = item)
            Label(fm, text = item, width = 8,
                height = 2).pack(side = 'left')
            
            #加入版面，padx:元件之間的水平距離，pady: 垂直間距
            fm.pack(side = 'left', padx = 2, pady = 10)

#產生物件
work = appWork()
# 顯示於視窗標題列
work.master.title('relief 常數值')
work.master.maxsize(1000, 400)
# 視窗訊息初始化
work.mainloop()
