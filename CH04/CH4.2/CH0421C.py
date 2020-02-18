# for廻圈配合range()擷取部份字串

word = 'They make a hourly wage'
print('字串長度:', len(word))

#表示依字串長度，從索引值0開始，每間隔2個字元做提取
for item in range(0, len(word), 3):
    print(word[item], end = '')
