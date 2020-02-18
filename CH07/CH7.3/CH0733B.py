#自訂函式
def score(name, n1, n2, n3):
    print(name)
    print('分數:', n1, n2, n3)
    total =  n1 + n2 + n3
    average = total/3    
    print('總分:',total,
          '平均:{0:.4f}'.format(average))

number = [78, 95, 53] #串列
#呼叫函式 -- number串列物件，可迭代
score('Toams', *number)

