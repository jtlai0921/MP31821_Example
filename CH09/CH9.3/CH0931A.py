import math, pprint

# 定義類別
class Circle:
    
    cnt = 0 #類別變數
    
    #__init__ 初始化物件    
    def __init__(self, radius = 15):
        self.radius = radius        
        Circle.cnt +=1
        
    def calcPerimeter(self):
        return 2 * self.radius * math.pi    
    
    def roundArea(self):
        return self.radius * self.radius * math.pi

#產生物件, 傳入半徑值
oneR = Circle()
print('圓的半徑:', oneR.radius)
twoR = Circle(13)
print('圓的半徑:', twoR.radius)
print('產生了{0}個物件'.format(Circle.cnt))

print('Circle.__name__ : ', Circle.__name__)
print('Circle.__doc__ : ', Circle.__doc__)
print('Circle.__module__ : ', Circle.__module__)



