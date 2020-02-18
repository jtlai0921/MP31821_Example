'''
   有規則的串列，3列 * 3欄，利用巢狀for來讀取
'''
number = [[11, 12, 13], [22, 24, 26], [33, 35, 37]]

for idx, one in enumerate(number): # 第一層for廻圈
   print('第{}列:'.format(idx), end = '')
   for two in one:  # 第二層for廻圈
      print(two, end = ' ') #輸出之後不換行
   print()   #完成第二層for廻圈之後換行
   
else:
   print('串列讀取完畢!')
