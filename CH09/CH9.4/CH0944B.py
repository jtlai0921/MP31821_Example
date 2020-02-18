#__getitem__() 並加人slice

class Student:
    score = [78, 56, 95, 87, 61]
    def __getitem__(self, index): #回傳索引編號
        print('索引值:', index, end = ' ')
        return self.score[index]

#建立物件
Mary = Student()
print('分數：', Mary[0])
