# Canvas元件繪製圖形
from tkinter import *

lastx, lasty = 0, 0 #座標

def position(event):#按滑鼠左鍵，取得位置
    global lastx, lasty #全域變數
    lastx, lasty = event.x, event.y
    
def addLine(event): #繪製線條
    global lastx, lasty
    cas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y #取得滑鼠目前位置
    
def cleanUp(event): #清除繪圖
    items = cas.find_all()
    for item in items:
        cas.delete(item)
        
root = Tk()
root.title('滑鼠繪製線條')
#依weight分配欄、列空間
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

cas = Canvas(root)
cas.grid(column = 0, row = 0, sticky =(N, W, E, S))
cas.bind("<Button-1>", position)#滑鼠左鍵
cas.bind("<B1-Motion>", addLine)#移動滑鼠
cas.bind("<Button-3>", cleanUp)#滑鼠右鍵

root.mainloop()
