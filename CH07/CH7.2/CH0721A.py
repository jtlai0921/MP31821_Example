'''
   Python傳遞引數依物件的可變和不可變做傳遞
   可變物件
'''
def passFun(name, score):
    print('自訂函式的形式參數')
    #字串不可變，接收的是複本
    print('name', id(name), end = ', ')
    #list是可變物件，接收的是記憶體位址
    print('score', id(score))

#呼叫函式
na = 'Mary'
sc = [75, 68]
passFun(na, sc)
print()
print('呼叫函式的實際引數')
print('na', id(na), end =', ') #不可變物件
print('sc', id(sc)) #可變物件
