#定義字典
data = {'x':78, 'y':56, 'z':92}

#自訂函式 -- 形式參數的x、y、z來自data的key
def student(n1, n2, n3, x, y, z): 
    print('%6s'%n1, '%3d'%x)
    print('%6s'%n2, '%3d'%y)
    print('%6s'%n3, '%3d'%z)

# 呼叫函式 -- 第3個實際引數為字典物件，前綴**
student('Eric', 'Tom', 'Ivy', **data)
