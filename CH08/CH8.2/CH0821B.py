#使用 __name__ 屬性

from random import randint

#產生10~100的整數亂數
number = randint(10, 100)

if __name__ == '__main__':
    print('我是主程式')
    
print('隨意數值：', number)
