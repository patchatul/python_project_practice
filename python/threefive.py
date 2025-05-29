import random
randomnum = random.randint(1, 101)
for i in range(1, 101):
    if i %3 == 0 and i %5 ==0:
        print(f"{i} is divided by 3 & 5")
    elif i % 3 ==0:
        print(f"{i} is divided by 3")
    elif i % 5 ==0:
        print(f"{i} is divided by 5")
    elif i == randomnum:
        print(f"{randomnum} and out")
        break
    else:
        print(i)