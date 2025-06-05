#tuples = ordered collections that cannot be changed once created. 
#They are ideal for storing fixed data that shouldn't change (e.g., coordinates, RGB color values).
#While lists can change, tuples cannot. This means tuples are immutable.
#However, you can replace one tuple with another and have duplicates within a tuple.
#Tuples are defined with or without parentheses and their items can be a mix of any data type
#If there is only one item, make sure there is a comma ,

friend1_location = (37.7749, -122.4194)    # San Francisco
friend2_location = (40.7128, -74.0060)     # New York
friend3_location = (4.624335, -74.063644)  # Bogota

tuples_friends = friend1_location +  friend2_location + friend3_location
print(tuples_friends)