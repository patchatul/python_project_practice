import random #generate username w/ functional programming 

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)
#capitalize suffix, map 
def capitalize_suffix(name):
  return name.capitalize()
cap_suffixes = list(map(capitalize_suffix, suffixes))
#list comprehension to generate 10 names
random_names = [create_fantasy_name(prefixes, cap_suffixes) for name in range(10)]
#if fire in name true
def fire_in_name(name):
  return 'Fire' in name
fire = list(filter(fire_in_name, random_names))
#name1+name2
def concatenate_names(name1, name2):
  return name1 + ', ' + name2
from functools import reduce
reduced_names = reduce(concatenate_names, fire )
#print generate name w/ for loop, include fire, reduced name
def display_name_info():
  print('Fantasy Names: ')
  for name in random_names:
    print(name)
  print('Filter name with \'Fire\': ', fire)
  for each in fire:
    print(each)
  print('Concatenated names: ', reduced_names)

display_name_info()
