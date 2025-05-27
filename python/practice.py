'''
hourUsed = int(input("Enter the KW hours used: "))
hourUsedOverThousand = hourUsed - 1000
dollarPerHour = 7.633 / 100
dollarPerHourOverThousand = 9.259 /100

if (hourUsed <= 1000):
    dollarPerKWHours = dollarPerHour * hourUsed
else:
    dollarPerKWHours = (1000 * dollarPerHour) +((hourUsed - 1000)*dollarPerHourOverThousand)
    
print(f"Amount owed is ${dollarPerKWHours}")
#1500 >>122.625 764>>58.31612 '''
'''

words = []

while True:
    word = input("Enter next word or quit: ")
    if word == "quit":
        break
    words.append(word)

line = ""

for i in range(len(words)):
    if i == len(words) - 1:
        line += f"and {words[i]}"
    else:
        line += f"{words[i]}, "

print(line) 
#one, two, and three
'''
'''
def LargestQuient():
    numbers = list(map(int, input("Enter integers separated by space (end with 0): ").split()))

    if numbers[-1] == 0:
        numbers.pop()

    print(max(numbers) //  min(numbers))
LargestQuient()
'''
'''
def WhereAmI():
    x,y = map(int, input("Enter X and Y separated by a space: ").split())
    if x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if y > 0:
            print("Q2")
        else:
            print("Q3")
WhereAmI()
'''
'''
def DifferenceTwoLists():
    numbers1 = list(map(int, input("Enter integers separated by space: ").split()))
    numbers2 = list(map(int, input("Enter integers separated by space: ").split()))
    result = []
    for i in range(len(numbers1)):
        if numbers1[i] not in numbers2:
            result.append(numbers1[i])
    for i in range(len(numbers2)):
        if numbers2[i] not in numbers1:
            result.append(numbers2[i])
    result=sorted(set(result))
    if result == []:
        print("No difference")
    else:
        print(result)
DifferenceTwoLists()
# 4 7 19 1 27 ,  5 7 23 14 9 27 >[1, 4, 5, 9, 14, 19, 23]

def SameTwoLists():
    numbers1 = list(map(int, input("Enter integers separated by space: ").split()))
    numbers2 = list(map(int, input("Enter integers separated by space: ").split()))
    result = []
    for i in range(len(numbers1)):
        if numbers1[i] in numbers2:
            result.append(numbers1[i])
    for i in range(len(numbers2)):
        if numbers2[i] in numbers1:
            result.append(numbers2[i])
    result=sorted(set(result))
    if result == []:
        print("No difference")
    else:
        print(result)
SameTwoLists()#[7, 27]
'''
'''
def GladToBeOne(num):
    seen = set()
    while num != 1:
        if num in seen:
            return False
        seen.add(num)
        num =sum(int(digit)**2 for digit in str(num))
        #print(num)
    return True
num = int(input("Enter a number: "))
if GladToBeOne(num):
    print("Glad to be one")
else:
    print("Not Glad")
    #49 >Glad
'''
'''
def LessToRight():
    data = list(map(int, input("Enter count, integers separated by a space: \n").split()))
    count = data[0]
    number = data[1:1 + count]
    result = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            if number[j] < number[i]:
                result +=1
                break
    print(result)
LessToRight()
#7 85 74 32 21 20 16 2 >6
'''
'''
def ItAddsUp():
    numbers =list(map(int, input("Enter int: \n").split()))
    target =numbers[0]
    numbers.pop(0)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(f'{numbers[i],numbers[j]} found at {[numbers.index(numbers[i])+1]}{[numbers.index(numbers[j])+1]}')
ItAddsUp()'''
'''
def RepeatNum():
    numbers = list(map(int, input("enter numbers: \n").split()))
    times = {}
    for number in numbers:
       if number in times:
            times[number] +=1
       else:
           times[number] =1
    for number, time in times.items():
        if time > 1: #just only repeated
            print(f"{number} occurs {time} times")
RepeatNum() #4 4 > 4 occurs 2 times'''
'''
def ZeroOut():
    numbers = list(map(int, input("enter numbers: \n").split()))
    notZero = []
    for number in numbers:
        if number != 0:
            notZero.append(number)
    for number in notZero:
        print(number)
ZeroOut()'''