# 以函式為物件

def show(): #函式，無參數
	print('Hello Python')

	
def InfoMsg(msg): #函式，1個形式參數
	msg()#呼叫函式

#呼叫函式InfoMsg()，以show為物件來作為實際引數
InfoMsg(show)
