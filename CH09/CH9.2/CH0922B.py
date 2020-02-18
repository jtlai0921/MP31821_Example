#定義類別 -- 利用__init__()方法來取得屬性並做輸出

class Motor:
    
    #__init__()：初始化物件
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    #定義方法二：輸出名稱和顏色
    def showMessage(self):
        print('款式:{0:6s}, 顏色:{1:4s}'.format(self.name, self.color))

# 產生物件
car1 = Motor('Vios', '極光藍')#物件1
car1.showMessage() #呼叫方法

car2 = Motor('Altiss', '炫魅紅')#物件2
car2.showMessage()
