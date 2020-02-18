# readline()方法讀取檔案

show = ''

with open('demo1201.txt', 'rt') as foin:
    
    print('檔案指標：')
    
    while True:
        print(foin.tell(), end = ' ')
        line = foin.readline()
        if not line:
            break
        show += line

