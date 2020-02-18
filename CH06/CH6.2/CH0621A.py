# defaultdict()建構式

from collections import defaultdict #匯入模組

df = defaultdict(int)  #以int為參數
print('以零為值：',df['One'],df['Two'])
df['Three'] = 3

#輸出時用dict()函式轉換
print('預設字典:', dict(df))
