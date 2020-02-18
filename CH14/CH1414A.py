# simpledialog - askinteger()方法
from tkinter import *

def processWord(): #處理輸入字串    
    name = simpledialog.askstring(title = '輸入字串',
            prompt = 'Your name: ')   
    print('名稱：', name)
   
def processInt(): #處理輸入整數值    
    score = []
    count = 0
    while True:
        number = simpledialog.askinteger(
            title = '輸入整數值', prompt = '分數: ',
            maxvalue = 100, minvalue = 60)
        score.append(number)
        count += 1
        if count == 5:
            break
    total = sum(score)    
    print('分數：', score)
    print('合計：', sum(score))
    
def processFloat(): #處理輸入浮點值    
    value = simpledialog.askfloat(title = '輸入浮點值',
            prompt = '含有小數的數值：', initialvalue = 5.888)   
    print('數值：', value)

#建立視窗物件
wnd = Tk()
wnd.title('simpledialog')
wnd.geometry('200x60+10+10')
#視窗物件加入按鈕
Button(text = '輸入字串', command = processWord).pack(
    side = 'left')
Button(text = '輸入整數', command = processInt).pack(
    side = 'left', padx = 5)
Button(text = '輸入浮點數', command = processFloat).pack(
    side = 'left')

mainloop()
