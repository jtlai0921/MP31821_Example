from io import open
import struct

#寫入二進位資料
with open('demo1206', 'wb') as fo:
    data = struct.pack('hhl', 2, 4, 7)
    print('二進位資料\n', data)
    fo.write(data)
    
#讀取二進位資料    
with open('demo1206', 'rb') as fo:
    value = struct.unpack('hhl', fo.read(8))
    print('Python資料：', value)    
    print('位元組大小：', struct.calcsize('hhl'))
