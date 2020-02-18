'''
   計算 2+4+...+20 偶數和，當計數器為10就離開廻圈
'''
sum = 0 #儲存累加值
for count in range(2, 20, 2):
   if count == 10:             
      break # 中斷廻圈的執行
   else:
      sum += count
      print('計數器 = ', count, ' 總和 = ', sum)
