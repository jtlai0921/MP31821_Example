'''
   datetime類別
'''
from datetime import datetime, date, time

#取得當前的日期和時間
now = datetime.now()

#取得年、月、日屬性, 以tuple物件回傳
print('日期：{}年{}月{}日'.format(now.year, now.month, now.day))

#取得時、分、秒屬性
print('時間：{}時{}分{}秒'.format(now.hour, now.minute, now.second))
