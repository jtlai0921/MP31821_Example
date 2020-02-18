# 二進位資料的寫入和讀取

ary = bytearray(range(5))
#二進位資料的寫入
with open('demo1205', 'wb') as fob:
    fob.write(ary)

#二進位資料的讀取
with open('demo1205', 'rb') as fob:
    fob.read(3)
    print(type(ary))
    print('二進位：', ary)
