# 在try/except敘述使用 raise敘述
def demo(data, num):    
    try:        
        data[num]
        
    except IndexError as err:
        print(err)
        raise IndexError('索引超出界值')
    
    else:
        print(data[num])

lt = ['Tom', 'Vicky', 'Steven']#List
demo(lt, 1)
demo(lt, 3)
