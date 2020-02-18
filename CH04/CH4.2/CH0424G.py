"""split(sep=None, maxsplit=-1)函式 -- 分割字串
   sep分割器，以空白字元做預設分割
   maxsplit 欲分割的數值 """
print("---split()函式分割字串---")

wordA = 'one tow three four'
print('原來字串:', wordA)

print('--預設值「空白字元」分割字串--')
#以預設值空白字元來分割字串，以list物件回傳
print(wordA.split())
#將字串分割成2+1
print('字串分割成3：', wordA.split(maxsplit = 2))

opr = '--'
opr *= 20
print(opr)
wordB = 'one, tow, three, four'
print('字串二：', wordB)
print('逗點分割字串', end = '->')
print(wordB.split(sep =',', maxsplit = 2))
