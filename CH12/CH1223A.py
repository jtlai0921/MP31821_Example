# read()方法讀取檔案
show = ''
#每次欲讀取的字元數
capacity = 80
with open('demo1201.txt', 'rt') as foin:
    while True:
        #讀取80個字元
        segment = foin.read(capacity)
        #顯示內容於螢幕
        print(segment, sep = '', end = '')
        #print(segment)
        if not segment:
            break
        show += segment
print('字元數：', len(show))
