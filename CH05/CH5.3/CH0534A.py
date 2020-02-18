'''
   不規則的串列，第一列串列中有3欄元素，
   利用巢狀for來讀取，執行時會發生錯誤
'''
number = [11, 13, [32, 34, 36, 38]]

for one in number: # 第一層for廻圈
   for two in one:  # 第二層for廻圈
      print(two, end = ' ') #輸出之後不換行
   print()   #完成第二層for廻圈之後換行
else:
   print('串列讀取完畢!')
