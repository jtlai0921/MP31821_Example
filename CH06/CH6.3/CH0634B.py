# 集合的數學運算(2) -- 產生新集合

st1 = {23, 24, 26}    #準備集合1
st2 = {23, 24, 33, 45}#準備集合2

print('差集計算 -- st1:', st1 - st2)
print('差集計算 -- st2:', st2 - st1)

print('差集-difference()方法')
print(st1.difference(st2))
print(st2.difference(st1))
print(st1.difference([78, 26, 91]))
print(st2.difference((33, 35, 21)))

# XOR 對等差集
print('對等差集', st1 ^ st2)

#對等差集 = (st1 – st2) | (st2 – st1)
print('對等差集-symmetric_difference()方法')
print(st1.symmetric_difference(st2))
print(st1.symmetric_difference([78, 24]))

