#快捷功能表
from tkinter import *
root = Tk()
root.title('Contextual Menus')
root.geometry('200x150')
#建立功能表物件
menuBar = Menu(root, tearoff = 0)
#產生功能表項目
for item in ('New File', 'Open', 'Save', 'Quit'):
    menuBar.add_command(label = item,
        font = ('Century Gothic', 14))
def popup(event): #回應滑鼠事件
    menuBar.post(event.x_root, event.y_root)
root.bind('<Button-3>', popup)#按滑鼠右鍵
