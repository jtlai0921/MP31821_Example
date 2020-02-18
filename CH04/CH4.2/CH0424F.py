#使用startswitch()和endswitch()方法

wd = 'Programming design'

print('字串:', wd)
#startswitch()未設start, end 只會搜尋整句的開頭
print('Prog?', wd.startswith('Prog'))
print('gram?', wd.startswith('gram', 0))

#startswitch()設start會依索引值搜尋
print('de?', wd.startswith('de', 12))

#endswitch()要搜尋非句尾的末端字元，同樣要設start或end參數才會依索引值做搜尋
print('ign?', wd.endswith('ign'))
print('ing?', wd.endswith('ing', 0, 11))

