# 建立類別，未使用__init__()方法

class Student():
    def score(self, s1, s2, s3):
        return (s1 + s2 + s3)/3

	
Tomas = Student()#產生物件
print('Tomas平均分數：',Tomas.score(78, 96, 55))

Tomas.subject = []
Tomas.subject.extend(['math', 'eng', 'computer'])
print(Tomas.subject)

