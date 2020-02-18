# 定義一個能判斷大小的函式

def bigValue(x, y):
   if x > y:
      result = x
   else:
      result = y
   return result

# 呼叫函式來判斷大小
num1, num2 = 15, 10
print('最大值', bigValue(num1, num2))
