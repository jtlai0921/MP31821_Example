#內部函式
def outer(x):
    def inner(y):
        return x ** y
    return inner

print(outer(5)(6))
