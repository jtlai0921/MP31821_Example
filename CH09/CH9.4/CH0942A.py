#重載運算子 __add__()，'+'左側運算元必須是物件

class Increase: #定義類別
    def __init__(self, num = 0):#初始化物件
        self.value = num
    def __add__(self, num):#兩數相加
        return self.value + num

n1 = int(input('Input Numbers:'))
# Increase.__init__(one, n1)
number = Increase(n1)
print(n1, '+ 12 = ', number + 12)
#print('12 + ', n1, '=', 12 + number)#會有錯誤
