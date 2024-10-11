names =['John', 'Ken', 'Sam']
print(names[-1]) #print Sam -1 as last element of list
print(names[-2]) #Ken
print(names[0].replace('John', 'Kim')) #Kim instead of John but names variable still be John
names[0] = 'Hun' #reassign names
names.append('Rain') #add element to list
names.insert(2, 'Paul') #['Hun', 'Ken', 'Paul', 'Sam', 'Rain']
names.reverse() #['Rain', 'Sam', 'Paul', 'Ken', 'Hun']
print(names) 
print('John' in names) #False
print(len(names)) # 5 items in list