from tkinter import *
#調色盤方塊呼叫 askcolor()方法 選擇色彩
def ChoiceColor():    
    tint = colorchooser.askcolor(title = '調色盤',
            initialcolor = '#FFAABB')    
    rgbs = tint[0]
    print('R: {:.3f}'.format(rgbs[0]))
    print('G: {:.3f}'.format(rgbs[1]))
    print('B: {:.3f}'.format(rgbs[2]))
    print('色彩16進位值:', tint[1])
#建立視窗物件
wnd = Tk()
wnd.title('colorchooser')
wnd.geometry('90x50+10+10')
#視窗物件加入按鈕
Button(text='調色盤', command = ChoiceColor).pack(
    side = 'bottom')
mainloop()
