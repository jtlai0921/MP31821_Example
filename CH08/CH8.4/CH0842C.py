'''
   使用datetime類別   
'''
from datetime import datetime, date, time

#datetime()建構式 -- 參數只有年、月、日
print('Date:', datetime(2016, 2, 5))

#datetime()建構式 -- 參數有：年、月、日, 指定時
print('Date 2:', datetime(2016, 2, 5, hour = 10))

#datetime()建構式 -- 參數：年、月、日時、分、秒
print('Date 3:', datetime(2016, 2, 5, 10, 35, 47))

print('', datetime.strptime(
    '2016-2-5 10:35:47', '%Y-%m-%d %H:%M:%S'))
