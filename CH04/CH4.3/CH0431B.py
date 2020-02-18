'''格式化字串'''
import math #匯入math模組

print("%.3f: 輸出含有3個小數位數的PI值")

#將輸出格式字串存放在變數裡
fmt = '含有4位小數：%.4f'
print('PI', fmt %(math.pi)) 
print("計算圓面積 PI*R*R")

radius = (math.pi)*5**2
print('圓面積:', radius)
print('圓面積', fmt % radius)
print('以4位整數輸出 -- %04d'%radius)
