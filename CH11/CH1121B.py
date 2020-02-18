#try/except敘述...Exception捕捉所有異常

tp = 25, 67, 12 #tuple
try:
    print(tp[3])
except IndexError as err:
    print('錯誤：', err)
