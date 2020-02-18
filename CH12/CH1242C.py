import json

class Motor:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        
# 建立物件
altis = Motor('Altizz', 'Gray', 1795)

#可序列物件為dump()方法的default參數值
def show(car):
    return{
        'Car'      : car.name,
	'Color'    : car.color,
	'Capacicy' : car.size
	}

altisJn = json.dumps(altis,
        sort_keys = True, default = show)
print('JSON\n', altisJn)

altisP = json.loads(altisJn)
print('dict 物件\n', altisP)

