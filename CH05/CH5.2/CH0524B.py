# List Comprehensions -- 不同的運算式

result = [x ** 2 for x in
          range(1, 5)]
print('平方數值：', result)

# 變更字母大小寫
wd = ['hello', 'python' ,'world']
print('原有字串：', wd)

newwd = [str.upper() for str in wd]
print('大寫字串：', newwd)
