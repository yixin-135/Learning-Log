import random

answer = random.randint(1,100)
num = 0
n = 0
while n != answer:
    n = int(input("请输入数字："))
    num += 1
    if n > answer:
        print(f"大了")
    elif n < answer:
        print(f"小了")
    else :
        print(f"猜对了，共{num}次")

