# 以內建函式print()編寫檔案

prose = '''
I made my song a coat
Covered with embroideries '''

fo = open('demo1202.txt', 'wt')
print(prose, file = fo,
      sep = '', end = '')
fo.close()
