'''
   datetime 計算兩個日期差異的天數
'''
from datetime import datetime, date, time
d1 = datetime.today()
d2 = datetime(2016, 5, 14)
dr = d2 - d1
print(dr.days, '天')
