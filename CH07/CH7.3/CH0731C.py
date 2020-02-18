'''
   「*tuple」物件之後加入關鍵字引數
   呼叫函式fun()，直接將參數「k」以關鍵字引數來傳遞
'''

#自訂函式
def fun(n1, n2, *t, k):
    print(n1, n2) #位置參數    
    print(k, t)#Tuple & 關鍵字引數

#呼叫函式
fun('Mary', 'score', 75, 63, k = True)

# 自訂函式 - 只有*字元，表示它不具名，不收集引數
def pern(name, *, pay):
    print(name, '月薪', pay)
    
#呼叫函式
pern('Mary', pay = 26500)
