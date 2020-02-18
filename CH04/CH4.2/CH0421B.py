#使用enumerate()加入索引值
word = 'good'
print(list(enumerate(word)))

week = ['Mon', 'Tus', 'Wed']

#將enumerate()的參數start設為1
print(list(enumerate(week, start = 1)))

#加入for廻圈
for idx, item in enumerate(week):
    print([idx], item, end = ' ')
