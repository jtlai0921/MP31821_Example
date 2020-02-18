'''
   計算 2+4+...+20 偶數和，當計數器為10就離開廻圈
'''
sum = 0 #儲存累加值
for count in range(2, 20, 2):
   if count == 10:             
      continue # 只中斷此次廻圈
   else:
      sum += count
      print('計數器 ={0:2d}, 總和 = \
         {1:2d}'.format(count, sum))
