'''裝飾器 -- 定義 Decorator
    *args -- 收集位置參數，**kw -- 收集關鍵字引數
'''
import time, functools

def Records(some_func): #裝飾器   
    @functools.wraps(some_func)    
    def inner(*args, **kw): #回傳函式
        print('Hi! 呼叫了{}()'.format(
            some_func.__name__))
        return some_func(*args, **kw)            
    return inner    

@Records #裝飾器
def Atonce():
    #將取得時間做格式化動作
    return time.strftime('%Y-%b-%d %H:%M:%S',
        time.localtime())

#呼叫函式
print('登入時間:', Atonce())
