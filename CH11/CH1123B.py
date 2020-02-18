# try/except用來捕捉例外

num1, num2 = eval(
        input('請輸入兩個數值，用逗點隔開：'))    
try:
    result = num1 / num2        
except ZeroDivisionError as ex1:
    print('Error:', str(ex1))
else:
    print('相除結果：', result)
        

