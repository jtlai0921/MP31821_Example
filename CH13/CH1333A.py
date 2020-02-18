#Text元件
from tkinter import *
root = Tk()
root.title('Text元件')
txt = Text(root, width = 40, height = 10)
txt.pack()

#設定Text的屬性來各別使用
txt.tag_config('ft_bold',
    font =('Verdana', 14, 'bold', 'italic'))

txt.tag_config('title', justify = CENTER,
    underline= 1, font =('Arial', 24, 'bold'))

txt.tag_config('tine', foreground = 'blue',
    font = ('Lucida Bright', 14))

txt.tag_config('bd', relief = GROOVE,
    borderwidth = 3, font = ('Levenim MT', 16))

# insert()方法從最後一個字元插入字串
txt.insert(END, 'A Coat\n', 'title')
txt.insert(END, 'I made my song a coat\n',
    'ft_bold')
txt.insert(END, 'Covered with embroideries\n',
    'tine')
txt.insert(END, 'From heel to throat\n', 'bd')
mainloop()
