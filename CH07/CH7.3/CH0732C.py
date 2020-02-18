'''
自訂函式 -- 形式參數
* 將位置引數放入串列
** 把關鍵字引數放入字典
'''

def student(name, *score, StdNo, **pern):
    print('名字:', name, ' 學號:', StdNo)
    # for廻圈讀取字典物件並配合內建函式sorted做排序
    for item in sorted(pern):
         print('{0:8s}{1:<}'.format(item, pern[item]))
    
    print('成績：', sorted(score))

#呼叫函式 
student('Tomas', 65, 78, 71, StdNo = '102HJ2501',
        Year = 104, have = '必修',
        Subject = 'Computer')
