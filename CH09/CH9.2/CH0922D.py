import math

# 定義類別
class Circle:
    '''
定義類別的方法
calcPerimeter : 計算圓周長
roundArea     : 計算圓面積
__init__()    : 自訂物件初始化狀態 '''
    
    #__init__ 初始化物件    
    def __init__(self, radius = 15):
        self.radius = radius        
    
    def calcPerimeter(self):
        return 2 * self.radius * math.pi    
    
    def roundArea(self):
        return self.radius * self.radius * math.pi

#產生物件, 傳入半徑值
firstR = Circle(17)

print('圓的半徑:', firstR.radius)
print('圓周長:{0:2f}'.format(firstR.calcPerimeter()))
print('圓面積:{0:3f}'.format(firstR.roundArea()))
