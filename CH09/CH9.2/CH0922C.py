#定義計算圓形的面積和周長的函式
import math

#算出圓周長
def calcPerimeter(radius):
    return 2 * radius * math.pi

#算出圓面積
def roundArea(radius):
    return radius * radius * math.pi

print('圓周長：{0:4f}'.format(
    calcPerimeter(15)))

print('圓面積：{0:4f}'.format(
    roundArea(15)))

