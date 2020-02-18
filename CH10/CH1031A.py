#定義抽象類別 - 匯入abc模組
from abc import ABCMeta, abstractmethod

class Person(metaclass = ABCMeta): #抽象類別    
    @abstractmethod #裝飾器 - 抽象方法
    def display(self, name):
        pass
    def pay(self):
        self.display(self.name, self.salary)
        
#實作Person類別
class Clerk(Person):
    
    def __init__(self):
        self.name = 'Setven'
        self.salary = 28000
    
    def display(self, name, salary):        
        print(name, 'is a Clerk')
        print('薪水：', salary)

#建立物件，呼叫抽象類別的一般方法pay()
steven = Clerk()
steven.pay()

