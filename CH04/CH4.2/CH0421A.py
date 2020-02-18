#for廻圈讀取字串, 輸出Hello
word = 'Hello'
print('輸出字串：', end = '')
for item in word:
    print(item, end = '')

# BIF enumerate()函式加入索引值
print('\n有索引編號的字串：')
for idx, item in enumerate(word):
    print([idx], item, end = ' ')
