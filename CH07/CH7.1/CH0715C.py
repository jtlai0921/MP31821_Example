#自訂函式 -- 以tuple物件儲存數值相加、相乘和相除結果

def answer(x, y):    
    return x+y, x*y, x/y
    
#呼叫函式
numA = int(input('輸入第一個數值:'))
numB = int(input('輸入第二個數值:'))
print('運算結果:\n', answer(numA, numB))

