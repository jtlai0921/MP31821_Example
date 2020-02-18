import random as rdm #匯入random模組

# 產生 1-10 之間的亂數
num1 = rdm.randrange(10) + 1
num2 = rdm.randrange(10) + 1
num3 = rdm.randrange(10) + 1

total = 0; result = 0
lst = [] #串列

if num1 == 7 or num2 == 7 or num3 == 7:
    
    # 配合range()函式隨機產生4個亂數
    for item in range(1, 5):
        # 隨機產生1~10整數亂數
        item = rdm.randint(1, 10)
        #append()方法將亂數加入串列
        lst.append(item) 
        result += item
        
    print('得到一個幸運號碼7，附加紅利：', lst)
    print('紅利和：', result)
    total = result + num1 + num2 + num3   
    print('點數：', total)
    
else:
    print('穫到點數：{0:2d},{1:2d},{2:2d}'.format(
        num1, num2, num3))
    total = num1 + num2 + num3
    print('紅利：', total)


 
