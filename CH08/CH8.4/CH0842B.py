#計算工作年資
from datetime import date, timedelta
tody = date.today() #今天日期

#到職日期
work = date(2004, 7, 12)
diff = tody - work

#輸出工作天數
print('工作天數：{:,}天'.format(diff.days))

result = diff/timedelta(days = 365)
print('{0:.2f}年'.format(result))

