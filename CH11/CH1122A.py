#try/except敘述，卻無法捕捉到異常

tp = 25, 67, 12 #tuple
try:
    print(tp(3)) #應用中括號tp[3]，卻使用tp(3)
except IndexError as err:
    print('錯誤：', err)
