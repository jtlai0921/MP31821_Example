# Unpacking的應用
# 建立串列
student = [['Mary', 55, 68, 74],
	   ['Tomas', 77, 95, 88],
	   ['Eric', 68, 91, 72]]
for(name, math, english, computer) in student:
	print('%6s'%name, '總分:',
              (math + english + computer))

