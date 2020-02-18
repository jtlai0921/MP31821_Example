# 配合tuple的索引编號，讀取序列元素
number = (32, 34, 36, 38, 40, 42) #Tuple

print('index element')

for item in range(len(number)):
   print ('%5d %7d' %(item, number[item]))
else:
   print('讀取完畢')
