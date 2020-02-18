# 自訂函式 -- 指定預設參數值, 回傳值為字典
def person(name, sex, city = 'Taipei'):
    return {'name':name, 'sex':sex, 'city':city}

'''
呼叫程式碼 -- 2個引數時
第3個引數以預設值，3個引數以新值取代舊值
'''

print('基本資料：傳入2個引數')
print(person('Judy', 'Female'))
print('基本資料：傳入3個引數')
print(person('Steven', 'Male', 'Kaohsiung'))
