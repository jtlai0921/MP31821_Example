"""count(sub[, start[, end]])函式 -- 計算wordA字串中o字元的出現次數
   sub欲計算字元
   start字元的開始位置，end字元的結束位置 """

wordB = 'one, tow, three, four'
print("\n---count()函式：計算wordA字串中o字元出現次數---")
print(wordB)
print('o字元出現的次數：', wordB.count('o'))
print('索引0~7字元0出現的次數：', wordB.count('o', 0, 7))

