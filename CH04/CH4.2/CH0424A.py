
"""find(sub[, start[, end]])方法 -- 回傳某字串首次出現的索引位置，找不到時回傳-1
   sub欲尋找字元或字串
   start字元的開始位置，end字元的結束位置 """

print("\n---find()函式：尋找字串中子字串all出現的位置---")
wordC = '''We all look forward to the annual ball  
           because it’s great time to dress up.'''
print(wordC)
print('all索引編號：', wordC.find('all')) #尋找all子字串，從索引編號0開始
print('第二個 all 索引編號：', wordC.find('all', 7)) #尋找子字串all，從索引编號7開始
print('Python索引編號：', wordC.find('Python')) #找不到子字串時，回傳-1值

"""index(sub[, start[, end]])方法 -- 回傳指定字元的索引值，找不到回傳ValueError
   sub欲尋找字元或字串
   start字元的開始位置，end字元的結束位置 """
print("\n---index()函式：尋找字串中子字串forward的索引編號---")
print('forward索引編號：', wordC.index('forward'))
# print(wordC.index('forwards')) #會找不到字串，回傳ValueError
