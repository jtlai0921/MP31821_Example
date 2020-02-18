'''
   index(x, i, j)
'''

data = 25, 17, 45, 6, 17 # 建立Tuple

# 找出第1個17的位置
print('數值17之索引編號：', data.index(17))

# 由索引編號2到最後，回傳第2個17的位置
print('第2個17：', data.index(17, 2))

#也可以這樣使用index()方法
print('以另外方法讀取')
print('data[0:4].index(17)--', data[0:4].index(45))

# 回傳錯誤訊息ValueError
#data.index(17, 2, 4) 

