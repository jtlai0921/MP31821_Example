# 使用關鍵字引數可減少一一對應

def pern(name, sex, tall, city):
    print('名稱', name)
    print('性別', sex, '身高',tall)
    print('居住地', city)

pern(city = 'Taipei', tall = 170,
     name = 'Steven', sex = 'Male')
