'''
   以雙層for/in廻圈產生九九乘法表   
'''
# 建立表頭
print('  |', end = '')
for k in range(1, 10):
   print('{0:3d}'.format(k), end = '') #不自動換行，只留空白字元
print()
print('-'*32)

# 第一層 for/in
for one in range(1, 10):
   print(one, '|', end = '')
   
   # 第二層 for/in
   for two in range(1, 10):      
      print('{0:3d}'.format(one*two), end = '')
      
   print() #換行
