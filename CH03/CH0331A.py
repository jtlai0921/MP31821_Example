# for廻圈配合range()函式，將數值1+2+3+...+10

sum = 0 #儲存加總結果

# 進入for/in廻圈
for count in range(11):  #1~10
   sum += count #將數值累加 
   print('累加值:', sum) #輸出累加結果
else:
    print('數值累加完畢...')
