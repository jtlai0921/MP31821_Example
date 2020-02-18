'''
   Python傳遞引數依物件的可變和不可變做傳遞
   可變物件
'''
def passFun(name, score):
    
    #只有內部的名字被改變
    name = 'Tomas'
    print('名字:', name)
    #新增一個分數，也影響函式之外的串列
    score.append(47)
    print('分數:', score)

#呼叫函式
na = 'Mary'
sc = [75, 68]
passFun(na, sc)
print(na, ': 分數', sc)


