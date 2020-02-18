'''
   將時間和日期兩個物件以combine()方法組合在一起
'''
from datetime import datetime, date, time
dt = date(2015, 5, 12)    #時間，取自date()建構式
tm = time(12, 50)         #日期，取自time()建構式

print('日期一：', datetime.combine(dt, tm))

print('日期二：', datetime.combine(dt, tm).strftime(
    '%Y-%m-%d %h:%M:%S'))   
