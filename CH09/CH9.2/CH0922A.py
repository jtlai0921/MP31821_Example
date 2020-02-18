#先建構，再初始化物件

class newClass:
    #__new__()建構物件
    def __new__(Kind, name):
        
        if name != '' :
            print("物件已建構")
            return object.__new__(Kind)
            
        else:
            print("物件未建構")            
            return None
            
    #__init__()初始化物件
    def __init__(self, name):
        print('物件初始化...')
        print(name)

x = newClass('')
print()
y = newClass('Second')
