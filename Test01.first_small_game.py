""" 用Python设计第一个游戏"""
import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("不妨猜一下现在我心里想的是哪个数字:")
    guess = int(temp)

    if guess == answer:
        print("你是肚子里的蛔虫吗？！")
        print("哼！猜中了也没奖励~~~！")
        break
    else:
        if guess < answer:
            print("小啦~")
        else:
            print("大啦~")
    counts = counts - 1
    
print("Game Over ^_^")
