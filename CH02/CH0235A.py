#使用分數

from fractions import Fraction #匯入fractions模組

num1 = Fraction(7, 8)
num2 = Fraction(12, 17)
#將兩個分數相加，輸出 215/136

print('分數相加', num1 + num2)

num3 = num1 * num2   #將兩個數相乘
print('num3:', float(num3))

print('分子',num3.numerator)   #取得分子，輸出21
print('分母', num3.denominator)    #取得分母，輸出34

