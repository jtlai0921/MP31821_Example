'''
   使用巢狀if敘述先判斷數值是否在1~12之間
   再以 if/elif 敘述依據值來顯示月份天數
'''
month = int(input('請輸入1~12月份：'))

# 第一層 if/else敘述 確認輸入月份在 1~12之間
if month >= 1 and month <= 12:
   # 第二層 if/elif敘述 
   if month == 4 or month == 6 or month == 9 \
         or month == 11:
      print('{0} 月有30天'.format(month))
   elif month == 2:
      print('{0} 月有28或29天'.format(month))
   else:
      print('{0} 月有31天'.format(month))
else:
   print('輸入月分不對，請重新輸入')
