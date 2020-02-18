# default()建構式 -- 統計字元數
from collections import defaultdict

wd = 'initially'
df = defaultdict(int)
for key in wd:
    df[key] += 1
print(list(df.items()))
