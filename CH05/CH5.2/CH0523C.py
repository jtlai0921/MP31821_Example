'''
   排序的兩種方法
   1.sorted()內建函式;  2.list.sort()由List提供的方法
'''
data = 258, 12, 37, 69, 47 #list物件
print('排序前：', data)
print('排序後：', sorted(data)) #排序，由小而大
print('原來資料不變：', data)

lst = list(data) #轉成list物件
line = '-----'
line *= 6
print(line)

print('轉成串列：', lst)
lst.sort(reverse = True)
convlt = tuple(lst)
print('由大而小排序：', convlt)
print('排序後已改變：', lst)
