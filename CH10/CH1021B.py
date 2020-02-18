#定義類別
class Motor: #基礎類別 或 父類別
    
    '''__init__: 初始化物件
       price, capacity 有預設值，表示是選項參數
    '''
    
    def __init__(self, name, price = 65,
                 capacity = 1500): 
        self.name = name 
        self.price = price 
        self.capacity = capacity       
  
    def equip(self, award):#配備加給
        self.price = self.price + award
        
    def __repr__(self): #設定輸出格式
        msg = '{0:8s}, 售價{1:7.2f} 萬,排氣量 {2:,} c.c.'
        return msg.format(
            self.name, self.price, self.capacity)
    
class Hybrid(Motor): #衍生類別 或 子類別   
        
    def equip(self, award, cell = 2.18):
        Motor.equip(self, award + cell)
        
    def tinted(self, opr):
        if opr == 1:
            return '極緻藍'
        elif opr == 2:
            return '魅力紅'        
    

#建立父類別物件
stand = Motor('standard') 
apollo = Motor('Apollo', price = 65.2,
               capacity = 1795)    
print(apollo, '不含電子鎖')    
apollo.equip(1.2) #加價

# 建立子類別物件
inno = Hybrid('Innovate', 114.8)
inno.equip(1.1)
print('Hybrid is', inno.tinted(2))

print('-- 三種車款 --')
for item in (stand, apollo, inno):        
   print(item)

