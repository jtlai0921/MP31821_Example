#類別的繼承

class Father: #基礎類別
    def walking(self):
        print('多走路有益健康!')
        
class Son(Father): #衍生類別
    pass

#產生子類別實體
Joe = Son()
Joe.walking()
