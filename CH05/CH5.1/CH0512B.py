'''
   使用while廻圈讀取tuple，必須設定計數器
'''
number = (21, 23, 25, 27 , 29)
item = 0 # 計數器，配合tuple的索引值，由0開始

# while廻圈
while item < len(number): # len()取得number的長度
   print(number[item], end = ' ')
   item += 1 #計數器累加
else:
   print('\n讀取完畢')
