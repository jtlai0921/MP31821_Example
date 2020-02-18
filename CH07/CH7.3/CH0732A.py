'''
   自訂函式中的2個形式參數
   第1個形式參數：位置參數，第2個以**配合dict物件
'''
def stud(name, **dt):
	print('Name:', name)
	print('Score:', dt)

#呼叫函式 -- 1個位置引數
stud('Mary')
stud('Tomas', eng = 65, math = 71, chin = 83)
