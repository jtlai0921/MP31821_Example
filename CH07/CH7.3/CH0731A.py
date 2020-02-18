'''
   星號運算式(stat expression)
   就是將*字元放在某個識別字名稱之前
'''
pern = ('David', 'Male', 95, 68, 72)#Tuple
name, sex, *score = pern    #Tuple拆解用法
print('Name:', name)    
print('分數: ', score)



