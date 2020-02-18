'''
   依日期找出上個星期所對應的日期
'''
from datetime import datetime, timedelta
#建立儲存星期的list物件
weeklst = ['Monday', 'Tuesday', 'Wednesday',
         'Thuusday', 'Fridat', 'Saturday', 'Sunday']
def getWeeks(wkName, beginDay = None):
    
    #如果未傳入beginDay之日期，就以今天為主
    if beginDay is None:        
        beginDay = datetime.today()
        
    #weekday()方法回傳指定日期的星期索引值，Monday索引值為0
    indexNum = beginDay.weekday()
    
    target = weeklst.index(wkName)
    
    #算出指定日期的星期值
    lastWeek = ( 7 + indexNum - target) % 7
    
    if lastWeek == 0:
        lastWeek = 7
        
    #timedelta()建構式取得天數
    lastWeek_Day = beginDay - timedelta(
        days = lastWeek)
    return lastWeek_Day.strftime('%Y-%m-%d')

#只傳入一個參數
print('今天的上週二：', getWeeks('Tuesday'))

#傳入二個參數
dt = datetime(2016, 3, 5)
print('2016/3/5 的上週六：', getWeeks('Saturday', dt))
