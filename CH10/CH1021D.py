#繼承的搜尋順序

class Parent(): #有兩個方法
    def show1(self):
        print("Parent method one")
        
    def show2(self):
        display("Parent method two")
        
class Son(Parent):
    def display(self):
        print('Son method')
        
class Daughter(Parent):
    def show2(self):
        print('Daugher method one')
        
    def display(self):
        goodNews('Daughter method two')
        
class Grandchild(Son, Daughter):
    def message(self):
        print('Grandchild method')
 
eric = Grandchild()
#先找到自己的方法
eric.message()
#依順序, Grandchild > Son
eric.display()
#Grandchild > Son > Daughter
eric.show2()
#Grandchild > Son > Daughter > Parent
eric.show1()
