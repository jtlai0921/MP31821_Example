class Testing():
    #初始化物件
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y    
    
    def __del__(self): #destructor - 用來清除物件
        MyName = self.__class__.__name__
        print('已清除', MyName)
#建立物件
t1 = Testing(15, 20)
t2 = t1
print('t1 = ', id(t1), ', t2 = ', id(t2))
del t1
del t2
