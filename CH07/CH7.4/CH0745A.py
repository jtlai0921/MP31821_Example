# 定義計算階乘的函式
def factD(x):
    upshot = 1 #儲存階乘計算結果    
    for item in range(1, x+1):
        upshot *= item
        #加入print()觀看階乘的變化
        #print('{0:2d}! = {1:,}'.format(item, upshot))
    return upshot

# 呼叫函式
n = int(input('輸入計算階乘的數值:'))
total = factD(n)
print('階乘{0:2d}!: {1:,}'.format(n, total))


# 以遞廻定義階乘
def factR(x):
    if x <= 1 : # 0! = 1! = 1
        return 1 # 基本情況，終止遞廻
    # 如果階乘是2(含)以上，自己呼叫本身的函式
    else:
        return (x * factR(x - 1))

print('遞廻：', factR(n))

