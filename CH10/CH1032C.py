from CH1041A import Motor, sportCar, Hybrid

class Vehicle(): #與三個類別無關聯
    def equip(self):
        return 2500 
    def show(self):
        return 'Qi無線充電座'

def unite(article):#定義方法來輸出各物件
    print('{:12s}, 售價 {:,} '.format(
        article.show(), article.equip()))

altiz = Motor('Altiz', 487500)
unite(altiz)
inno = sportCar('Innovate', 638000)
unite(inno)
suv = Hybrid('SUV', 1150000) #子類別物件
unite(suv)

car = Vehicle()#Vehicle 物件
unite(car)

