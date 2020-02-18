'''
   使用自訂函式，配合*tuple收集引數的值，
   還能指定關鍵字引數
'''
#自訂函式
def student(name, *score, subject = 4):
    if subject >= 1:
        print('名字：', name)        
        print('共有', subject, '科, 分數：', score)
    total = sum(score)
    print('總分：', total,
          ', 平均:', '%.4f'%(total/subject))
 
#呼叫函式
student('Tomas', 78, 65, 93, 81)
student('Mary', 65, 90, 57, subject = 3)
