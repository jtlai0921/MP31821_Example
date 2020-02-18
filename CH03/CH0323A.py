'''
   使用if/elif敘述做多重條件半斷，依據輸入分數來判斷應顯示的等級
'''
score = int(input('請輸入分數：'))

#進入if/elif敘述判斷
if score >= 60:
   print('{0:<3d}表現持平！'.format(score)) #欄寬3，<向左對齊
elif score >= 70:
   print('{0:<3d}不錯噢！'.format(score))
elif score >= 80:
   print('{0:<3d}好成績'.format(score))
elif score >= 90:
   print('{0:<3d}非常好'.format(score))
else:
   print('{0:<3d}請多多努力！'.format(score))
