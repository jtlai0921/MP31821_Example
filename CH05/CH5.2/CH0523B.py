#tuple物件以sort()方法排序

tp = 12, 178, 34, 92
print('Tuple排序前的元素：', tp)

#1.以list()函式轉為list
covlt = list(tp)
#2.以list.sort()方法做排序
covlt.sort()
#3.tuple()函式將排序的list再轉成tuple
covtp = tuple(covlt) 
print('Tuple排序後的元素：', covtp)
