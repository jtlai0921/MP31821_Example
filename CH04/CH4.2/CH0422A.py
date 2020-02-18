'''
   1.[start : end]
   2.[start : end : step]
'''

msg = 'Hello Python!'
#使用正值索引
print('原來字串：', msg)
print('msg[6:] =', msg[6:])
print('msg[:5] =', msg[:5])
print('msg[4:8] =', msg[4:8])
print('msg[0:10:2] =', msg[0:10:2])

#使用負值索引
print('msg[-7:-1] =', msg[-7:-1])
print('msg[-7:] =', msg[-7:])

#Stride slices
print('反轉字元 msg[::-1] =', msg[::-1])
print('msg[::-2] =', msg[::-2])
print('msg[-2:1:-3] =', msg[-2:1:-3])
