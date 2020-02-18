#全域變數加註global關鍵字

fruit = 'Orange' #全域變數

def summer():
    global fruit
    print('Favorite fruit is', fruit)
    fruit = 'Watermelon'
    print('Summer fruit is', fruit)

#呼叫函式 -- 同時輸出全域、區域變數fruit的值
summer()

