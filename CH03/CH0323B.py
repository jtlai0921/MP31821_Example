'''
   以if/elif來判斷月份天數
'''
month = int(input('請輸入1~12月份：'))

# if/elif敘述 配合or邏輯運算子
if month == 4 or month == 6 or month == 9 or month == 11:
   print(month, '月有30天')
elif month == 2:
   print(month, '月有28或29天')
else:
   print(month, '月有31天')
   

