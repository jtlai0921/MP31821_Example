#自訂函式中不能改變全域變數的值

fruit = 'Orange' #global變數
def summer():
    #print('Favorite fruit is', fruit)#拿掉註解會發生錯誤
    fruit = 'Watermelon' # Local變數
    print('Summer fruit is', fruit)

#呼叫函式
summer()
