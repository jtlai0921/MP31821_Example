#定義費氏數列
'''
def fiboR(n, fib = [0, 1]):
    if n >= len(fib):    
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]
    
#呼叫函式
print('Fibonacci:', fiboR(10))
'''

#費氏數列 -- 遞迴函式
def fibon(x):
    if x <= 1:
        return x
    else:
        return fibon(x - 1) + fibon(x-2)

#呼叫函式
outcome = []
print('以遞迴處理費氏數列:')

for item in range(10):    
    outcome.append(fibon(item))

print(outcome)
