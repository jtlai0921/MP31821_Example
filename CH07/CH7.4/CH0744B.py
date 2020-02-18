#使用filter()函式
#example 1 -- 定義簡單的函式
def getNums(x):
    return x > 2

# 可迭代物件，以range()函式產生
lt = range(10)
#所得結果以List轉換
print(list(filter(getNums, lt)))

# example 2
lst = range(1, 16)
print('被3整除的數值：\n',
    list(filter(lambda x : x % 3 == 0, lst)))

