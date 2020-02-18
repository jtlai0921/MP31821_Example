# Unpacking應用

tp = 15, 30 #tuple
one, two = tp #Unpacking
print('Before swap:{}, {}'.format(one, two))
one, two = two, one
print('After swap:{}, {}'.format(one ,two))
