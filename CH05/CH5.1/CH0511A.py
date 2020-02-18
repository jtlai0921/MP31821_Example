'''
   產生tuple物件
   配合+運算子做串接，*運算子做複製
'''

tp1 = (11, 33); tp2 = (22, 43)
print('tuple1:{0}, tuple2:{1}'.format(tp1, tp2))
print('串接:', tp1 + tp2)

# 將左、右兩個元素相加
tp3 = 'one', 'two' + '-Tomas', 'three'
print('tuple3:', tp3)

#*複製tuple
print('tuple1複製', tp1 * 2)
wd = 'AbCd'
print('複製前:{0}, 複製後:{1}'.format(wd, wd*3))

