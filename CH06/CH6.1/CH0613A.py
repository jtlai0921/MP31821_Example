'''
   字典操作
'''
score = {11:'Mary', 12:'John', 13:'Andy', 14:'Bob'}
print('字典:');  print(score)
print('Score長度：', len(score)) #回傳字典長度

del score[14] #刪除score[14]
print('刪除key 14'); print(score)

print('Key 12 in Score?', 12 in score)
print('Key 14 in Score?', 14 not in score)

#使用for廻圈讀取key輸出對應的value
for key in iter(score):
    print('%2d:%4s '%(key, score[key]), end =' ')
