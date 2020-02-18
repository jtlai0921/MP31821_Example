# readlines()方法讀取一行並回傳一行
with open('demo1201.txt', 'rt') as foin:
    total = foin.readlines()
#取得行數，再以for廻圈讀取
print('行數：', len(total))
for line in total:    
    print(line, end = '')                
         
