# 自訂函式，第一個位置參數，第二個則是預設參數

'''
def tax(rate = 0.08, price): #產生SyntaxError
    return price + price*rate 
'''

def tax(price, rate = 0.08):
    return price + price*rate

#呼叫函式 -- 只有一個引數
cost = int(input('請輸入價格：'))
print('含稅價格：', tax(cost))
