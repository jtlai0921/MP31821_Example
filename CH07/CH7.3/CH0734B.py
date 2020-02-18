#自訂函式 -- 形式參數的x、y、z來自字典物件data的key
def student(n1, n2, n3, x, y, z): 
    print('%4s'%n1, '%4d'%x)
    print('%4s'%n2, '%4d'%y)
    print('%4s'%n3, '%4d'%z)
    print('-'*15)
    print(' 總分', '%4d'%(x + y + x))

#定義字典
data = {'x':78, 'y':56, 'z':92}

# 呼叫函式 -- 第3個實際引數為字典物件，前綴**
student('1st', '2nd', '3rd', **data)
