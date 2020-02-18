
class Numbers:
    def __init__(self, value = None):
        self.num = value
        self.result = 10        
        
    def increase(self):
        self.result += self.num
        return self.result
    
    def subtract(self):
        self.result -= self.num
        return self.result

one = Numbers(5)
print("增加：", one.increase())
print("減少：", one.subtract())
print("第二次減少：", one.subtract())
