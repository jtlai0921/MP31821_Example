#字典的操作
number = {'Grace':68, 'Tom':76} #字典
number['Eric'] = 85 #新增一個項目

number.setdefault('John')
print('成績：', number) #key-2 value-None
number['John'] = 45 #設定John的分數

#以update()方法加入已配對物件
number.update({'Andy':93, 'David':93})

#將分數排序
print('依名字排序')
for key in sorted(number):
    print('%-10s %d' % (key, number[key]))

number.pop('David')#刪除David
print('依名字遞減排序')
for value in sorted(number, reverse = True):
    print('%-10s %d' % (value, number[value]))

print('字典清空 -- ', number.clear())
score = {'Judy':63, 'Sunny':60}
number.update(score) # 將另一個字典物件加入
number.update(Steven = 87, Ivy = 74)#以指派方式更新
print('更新字典內容：\n', number)
