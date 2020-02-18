#自訂函式 -- 形式參數採用預設值

def getColor(item, color = None):
    
    # 用is運算子判別color是否為None
    if color is None:
        color = []
        
    color.append(item) #append()方法新增 list 元素
    print('顏色：', color)

#主要敘述
key = input('y 繼續..，n 結束廻圈..:')

while key == 'y':
    wd = input('輸入顏色：')
    getColor(wd) #呼叫自訂函式
    
    key = input('y 繼續..，n 結束廻圈..:')

