# 將有序字典排序

from collections import OrderedDict

stud = {'Mary':87, 'Eric':49, 'David':81,
      'Peter':72, 'Judy':67}

#BIF sorted()函式，使用key排序
name = OrderedDict(sorted(
    stud.items(), key = lambda fd: fd[0]))
print('名字做遞增排序')
for key in name:
    print('%5s'%key, name[key])

print('----------')
print('分數做遞減排序')
#BIF sorted()函式，使用value排序
score = OrderedDict(sorted(stud.items(),
        key = lambda fd: fd[1], reverse = True))

for key in score:
    print('%5s'%key, score[key])
