'''
   利用while迴圈計算總分和平均值，輸入-1結束廻圈
'''
sum = score = 0 # sum儲存總分，score儲存分數設初值為0
count = -1 #計數器

# 進入while廻圈
while score != -1: 
   score = int(input('輸入分數：')) #以int()函式轉為整數
   sum += score
   count += 1
average = sum / count # 計算平均值
print('共', count, '科，總分:', sum,', 平均:',average)
