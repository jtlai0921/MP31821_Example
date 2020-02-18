'''
   將日期以運學方式做運算
'''
from datetime import datetime, timedelta

d1 = datetime(2015, 7, 8)
print('日期：', d1 + (timedelta(days = 7)))

d2 = datetime(2016, 4, 25)
d3 = timedelta(days = 105)
dt = d2 - d3 #將兩個日期相減
print('日期二：', dt.strftime('%Y-%m-%d'))
print('以年、週、星期回傳', dt.isocalendar())


