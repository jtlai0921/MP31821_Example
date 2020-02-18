# 取得移動中的滑鼠座標
from tkinter import *

def motion(event): #取得移動中的滑鼠座標
    print('滑鼠座標: x-{} y-{}'.format(event.x, event.y))
    return

wnd = Tk()
wnd.title('Event Motion')
Yeats = '''
Be you still, be you still, trembling heart;
Remember the wisdom out of the old days: 
\n(To his Heart, bidding it have no Fear)'''
show = Message(wnd, text = Yeats)
show.config(bg = 'sky blue',
    font =('Century Gothic', 20, 'italic'))
show.bind('<Motion>', motion)
show.pack()
mainloop()
