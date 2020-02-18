'''
   處理字串大小寫的方法
'''
word = 'HELLO WORLD PYTHON'
print('原來字串：', word)
print('第一個單字的首字元大寫', word.capitalize()) #只有第一個字元會大寫
print('單字首字會大寫', word.title()) #單字開頭第一個字元會大寫
print('全部轉為小寫字元', word.lower()) #轉為小寫
print('是否皆為小寫字元', word.istitle()) #由於都是大寫字元，所以回傳False
print('是否皆為大寫字元', word.isupper()) #皆為大寫字元，回傳True
print('是否皆為小寫字元', word.islower()) #是否皆為小寫字元，回傳False

