from pprint import pprint, pformat

dt = {'Mary Hansen': (1988, 'Kaohsiung', 'Female'),
      'Bernard Webber': (1992, 'Taipei', 'Male'),
      'Charles Nickerson': (1998, 'Kaohsiung', 'Male')}

print('一般輸出')
print(dt)

print()
print('pprint()方法，只有object參數')
pprint(dt)

print()
print('參數：width = 60')
pprint(dt, width = 60)

print()
print('參數：width = 40, depth = 1')
pprint(dt, width = 40, depth = 1)

print()
print('參數：width = 40, depth = 2')
pprint(dt, width = 40, depth = 2)

print()
print('參數：width = 40, depth = 2, compact = True')
pprint(dt, width = 40, depth = 2, compact = True)


