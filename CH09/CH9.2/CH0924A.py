#特殊方法 __str__(): 

class Birth():
    
    def __init__(self, name, y, m, d):
        self.title = name
        self.year = y
        self.month = m
        self.date = d
        
    # 定義輸出格式    
    def __str__(self):
        print('Hi!', self.title)
        return 'Birth - ' + str(
            self.year) + '年' + str(
            self.month)+ '月' + str(
            self.date) + '日'
    
    # 呼叫format()方法做格式化輸山
    def __repr__(self):
        return '{}年 {}月 {}日'.format(
            self.year, self.month, self.date)

#產生物件
p1 = Birth('Grace', 1987, 12, 15)
print(p1)
print(p1.title, 'birth day: ', repr(p1))

		
