#List Comprehension

numA = [] #空的串列

for item in range(10, 50):
    if(item % 7 == 0):
        numA.append(item) #整除者放入List裡
print('10~50被7整除之數：', numA)

# List Comprehension
numB = [] #空的List
numB = [item for item in range(10, 50)
          if(item % 9 == 0)]
print('10~50被9整除之數：', numB)
