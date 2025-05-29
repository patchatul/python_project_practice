gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
print("Find out if you are Gryffindor, Ravenclaw, Hufflepuff, or Slytherin")

question1 = int(input("Do you like Dawn or Dusk?\n 1)Dawn\n 2)Dusk\n "))
if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("wrong input")


question2 = int(input("When I'm dead, I want people to remember me as:\n 1)The Good\n 2)The Great\n 3)The Wise\n 4)the Bold\n "))
if question2 == 1:
    hufflepuff +=2
elif question2 == 2:
    slytherin += 2
elif question2 ==3:
    ravenclaw +=2
elif question2 == 4:
    gryffindor += 2
else:
    print("wrong input")

question3 = int(input("Which kind of instrument most pleases your ear?\n 1)The violin\n 2)The trumpet\n 3)the piano\n 4)The drum\n "))
if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 ==3:
    ravenclaw +=4
elif question3 == 4:
    gryffindor += 4
else:
    print("wrong input")
house_dict = {gryffindor:"Gryffindor", ravenclaw:"Ravenclaw", hufflepuff:"Hufflepuff", slytherin:"Slytherin"}
house = house_dict.get(max(house_dict))
print(f'Your house is {house}!')
print(f'Your scorces are Gryffindor: {gryffindor}, Ravenclaw: {ravenclaw}, Hufflepuff: {hufflepuff}, Slytherin: {slytherin}')