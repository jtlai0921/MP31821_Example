from tkinter import Tk, Label # 步驟1：匯入tkinter模組

# 步驟2：產生Tkinter主視窗物件 - root元件
Wnd = Tk()

# 步驟3：主視窗加上一個標籤來顯示文字
lblShow = Label(Wnd, text = 'Hello Python',
        width = 20, height = 4,
        fg = 'white', bg = 'gray')

# 步驟4：將標籤放入容器中
lblShow.pack()
