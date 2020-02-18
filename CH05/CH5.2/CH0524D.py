# 兩個串列寫成生成式

wd1 = ['2015'] #List - year
wd2 = ['Jan', 'Feb', 'Mar'] # List - month

# List Comprehensions
print('List Comprehensions\n',
       [(y, m) for y in wd1 for m in wd2 ])
'''
print('\n'.join(['%5s/%3s'%((y, m))
                 for y in wd1 for m in wd2]))
'''

# double for/in
combin = [] #List
for y in wd1: #讀取第一個串列
     for m in wd2: #讀取第二個串列 
         combin.append((y, m))

print('雙層for/in讀取：\n', combin)
