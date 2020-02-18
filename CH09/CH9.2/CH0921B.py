#定義類別, 傳入不同型別

class Student:
    def message(self, name): 
        self.data = name
        
    def showMessage(self):
        print(self.data)

s1 = Student()
s1.message('James McAvoy')
s1.showMessage()

s2 = Student()
s2.message(78.566)
s2.showMessage()
