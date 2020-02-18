#自訂函式 -- 關鍵字引數

def factorial(port, begin):
    result = begin #階乘的開始值
    for item in port:
        result *= item #讀進數值並相乘
    return result

#呼叫函式，指派引數
outcome = factorial(port = [3, 5, 7, 11], begin = 1)
print('數值 3, 5, 7, 11 相乘結果:',
      '{:,}'.format(outcome))

    
