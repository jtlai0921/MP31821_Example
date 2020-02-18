#定義一個圓形類別
import math
from CH1133A import MyError

class Circular:
    def __init__(self, radius):
        self.setR(radius)
        
    def getR(self): #取得半徑值
        return self._radius
    
    def setR(self, radius): #設定半徑值
        if radius > 0:
            self._radius = radius
        else:            
            raise MyError(radius)
        
    def periphery(self): #計算圓周長     
        return 2 * self._radius * math.pi
    
    def calcArea(self):        
        return self._radius * self._radius * math.pi
    
    def __repr__(self): #設定輸出格式
        return '圓周長: {:4.3f}, 圓面積：{:4.3f}'.format(
            self.periphery(), self.calcArea())

try:
    one = Circular(15)#物件1
    print(one)
    two = Circular(-11)#物件2
    print(two)    
except MyError as err:
    print()
    print('引發異常, 錯誤值:', err.radius)
    



       
