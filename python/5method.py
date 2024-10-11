first = "OctoBer TenTh 2024"
print(first.capitalize()) #October tenth 2024
print(first.upper()) #OCTOBER TENTH 2024
print(first.lower()) #october tenth 2024
print("2024" in first) #True means find "2024" in variable
print(first.find("t")) #2 means find t in place 3 
print(first.find("T")) #8 means find T in place 9 include blank space
print(first.find("b")) #-1 means no b in variable even there's B (case sensitive)
print(first.replace("TenTh","tenth")) #OctoBer tenth 2024
print(first) #the variable is still the same as it's immutable except reassign
first = "Eleventh" #reassign change value of variable
print(first) 
print(len(first)) #8 

print(2/1) #2.0 float
print(2//1) #2 int
print(2%1) #modulus
print(5 >=5 and 5 == "5") #False