# Local function
def exter(x, y):
    def internal(a, b):
        #BIF divmod() a//b, a % b 
        return divmod(a, b)
    #呼叫函式以它為物件，將x、y接收的值再傳給internal()函式的參數a、b
    return internal(x, y)

print(exter(25, 7))
