'''
   串列中有串列時，可以利用巢狀for讀取
   配合 isinstance()函式判斷是否為串列
'''

# 串列中有串列
student = ['Tomas', [78, 96, 92],
           'Mary', [77, 61, 54],
           'Graham', [64, 82, 79]]
print('%8s %s %2s %2s %3s %4s' %(\
   'Name', '國文', '英文', '數學', '總分', '平均'))

for outer in student: # 第一層for廻圈
   
   #判斷outer讀進來的是元素，還是串列
   if isinstance(outer, list):
      
      for inner in outer:  #第二層for廻圈       
         print('%4d'%(inner), end = '')
      
      print('%5d %6.2f'%(sum(outer), \
            sum(outer)/3), end = '')
      print() #換行
      
   else: # 非串列，直接輸出其元素
      print('%7s:'% (outer), end = '')
      
else:
   print('分數計算完畢')

   

