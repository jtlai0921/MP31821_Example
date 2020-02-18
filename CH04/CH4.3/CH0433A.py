# 欄位配合format()方法
from decimal import Decimal

print('二個關鍵字引數:')
print('{prog} was conceived in the late {year}s'\
    .format(prog = 'Python', year = 1980))

print('一個位置一個關鍵字引數：')
print('The {prog} was {0}'.format(34, prog = 'Python'))

#{欄名 ! 轉換}
print('{0} {0!s} {0!r} {0!a}'.format(Decimal(28.5)))
