#將函式的參數相乘

def multip(num1, num2):
    print('兩數相乘', num1 * num2)

#有三個參數 -- func 呼叫函式, one, two 位置參數
def handle(func, one, two):
    func(one, two)

#呼叫函式時，也呼叫了multip，而數值4, 7會傳入做相乘
handle(multip, 4, 7)
