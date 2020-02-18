'''
   使用格式字串%物件
'''
import math
word = 'Python'
print('I love %s'%word) # 1個格式字串

# 使用2個格式字串
print('%s was conceived in the late %ds'%(word, 1980))

# 加入欄寬和精確度
print('%4d'%25)
print('PI =', math.pi)
print('PI = %.4f'%math.pi)
