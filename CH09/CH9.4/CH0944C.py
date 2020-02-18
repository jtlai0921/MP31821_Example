#__getitem__()用於迭代索引

class Student():
    def __getitem__(self, k):
        return self.data[k]

#建立物件
one = Student()
one.data = 'Chicage'
print(one[1])
for item in one:
    print(item, end = ' ')
