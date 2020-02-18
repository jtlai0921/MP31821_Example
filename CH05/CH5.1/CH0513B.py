# Unpacking -- list, tuple物件

lst = [11, 56, 23] #list
one, two, three = lst #Unpacking
print('List:{0:3d},{1:3d},{2:3d}'.format(
    one, two, three))

# Packing & Unpacking
x = 'Mary'; y = '1995/4/3'; z = 165
tp = (x, y, z) #Packing
name, birth, tall = tp #Unpacking

print('名字：{0:>4s}'.format(name))
print('生日：{0:9s}, 身高：{1}'.format(birth, tall))
