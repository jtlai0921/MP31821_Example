#try/except敘述，except敘述列示多個異常型別

tp = 25, 67, 12 #tuple
try:
    print(tp(3)) #應用中括號tp[3]，卻使用tp(3)
except (IndexError, TypeError) as err:
    print('錯誤：', err)

