#以dict()來產生字典

# 關鍵字引數
print('關鍵字引數：\n',
      dict(name = 'Tomas', age = 20, sex = 'Male'))

# 串列中以序對分組(Sequence物件)
print('List以Tuple分組：\n',
      dict([('one', 1), ('two', 2), ('three', 3)]))
      
# 使用字典物件
print('字典物件：\n',
      dict({'Jan':1, 'Feb':2, 'Mar':3}))

#使用zip()函式
weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday']
number = ['1st', '2nd', '3rd', '4th',
          '5th', '6th', '7th']

wkcomb = dict(zip(number, weeks))
for key in wkcomb:
    print('%3s:%9s'%(key, wkcomb[key]))


