'''
   利用timedelta建構式可以將時間做轉換
'''
from datetime import datetime, timedelta
d1 = timedelta(days = 3, hours = 6)
d2 = timedelta(hours = 3.2)
dr = d1 + d2


print(dr.days, '天')
print('9.2時 = ', dr.seconds, '秒')
print('3天9.2時 = ', dr.total_seconds(), '秒')
