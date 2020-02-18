#自訂函式
def number(n1, n2, n3, n4, n5):
    print('Number:',n1, n2, n3, n4, n5)

#呼叫函式 *使用可迭代物件
print('後2個是可迭代物件')
number(11, 12, *range(13, 16))

print('前3個是可迭代物件')
number(*range(21, 24), 24, 25)

print('中間2個是可迭代物件')
number(31, *range(32, 34), 34, 35)
