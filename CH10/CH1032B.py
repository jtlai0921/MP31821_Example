#匯入CH1041A，輸出三個物件

from CH1032A import Motor, sportCar, Hybrid

altiz = Motor('Altiz', 487500) #父類別物件
print('{:8s} 定價 {:,}'.format(altiz.show(), altiz.equip()))

inno = sportCar('Innovate', 638000) #子類別物件
print('{:8s} 定價 {:,}'.format(inno.show(), inno.equip()))

suv = Hybrid('SUV', 1150000) #子類別物件
print('{:8s} 定價 {:,}'.format(suv.show(), suv.equip()))

