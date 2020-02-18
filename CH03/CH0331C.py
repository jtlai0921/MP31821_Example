# for廻圈配合range()函式，將數值奇數相加
sum = 0 #儲存加總結果

# 進入for/in廻圈
for count in range(1, 100, 2):  #1,3,5 ~ 99
   sum += count #將數值累加   
   
print('奇數累加結果', sum) #輸出累加結果
