# while廻圈將數值累加

sum = 0 #儲存加總結果
count = 1 #計數器

# 進入while廻圈
while count <= 10:  #1,3,5 ~ 99
   sum += count #將數值累加
   count += 1 #累加計數器
   
print('1+2+3+..+ 10 累加結果', sum) #輸出累加結果
