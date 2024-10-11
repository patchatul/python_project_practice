weight = input("Weight: ") #weight = float(input())
unit = input("Kg or Lbs: ")
if unit.upper() == "K":
    convert_unit = float(weight) / 0.45
    print("Weight in Lbs is " + str(convert_unit))
else: 
    convert_unit = float(weight) * 0.45
    print("Weight in Kg is " + str(convert_unit))