# 集合的數學運算 -- 產生新集合

st1 = {23, 24, 26}    #準備集合1
st2 = {23, 24, 33, 45}#準備集合2

print('聯集計算', st1 | st2)  #聯集計算

#使用union()方法
print('聯集-使用union()方法')
print(st1.union(st2)) #st1 | st2
print(st1.union([11, 18, 15]))    #以List為聯集對象
print(st1.union('One', ('Two', 25)))    #可以多個參數

#交集計算
print('交集計算', st1 & st2)
print('交集-intersection()方法')
print(st1.intersection(st2))
print(st1.intersection((24, 33, 98)))
