#index運算
class Group:
    def __getitem__(self, index): #重載index之值
        return index ** 2
#建立物件
it = Group()
print('Index:', it[2])
for item in range(1,4): #讀取index值
    print(it[item], end = ' ')
