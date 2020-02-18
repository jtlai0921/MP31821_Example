# mode: xt -- 避免檔案被覆寫
try:
    with open('demo1202.txt', 'xt') as fo:
        fo.write('暫停一下!!')
except FileExistsError:
    print('已有此檔案，不能覆寫')
