# 物件的屬性

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Hi! ', self.name)
        print('Your age: ', self.age)

#產生物件

p1 = Person('Vicky', 25)
p1.display()
print('年齡：', getattr(p1, 'age'))
setattr(Person, 'sex', 'Female')
print('性別：', p1.sex)
