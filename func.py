'''def div_by_2(x):
    return x/2
display_results = map(div_by_2, [1,2,3,4])
print(list(display_results))

def filter_even(x):
    return x%2 ==0
even_num = filter(filter_even, [1,2,3,4])
print(list(even_num))

from functools import reduce #cumulative multiply
def multiply(x,y):
    return x*y
product = reduce(multiply, [1,2,3,4])
print(product)
'''

#challenge
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
#filter song longer than 5 mins
def longer_than_five_minutes(x):
    return x[1] > 5.00
min = list(filter(longer_than_five_minutes, playlist))
print(min)
#map from min to sec
def minutes_to_seconds(x):
    time = x[1] 
    minutes = int(time)
    seconds = (time-minutes)*100
    seconds_song = (minutes *60) + round(seconds)
    return seconds_song
min_to_sec = list(map(minutes_to_seconds, playlist))
print(min_to_sec)
#add all mins
from functools import reduce
def add_playtime(y, x):
    song = x[1]
    return song + y
total_playtime = reduce(add_playtime, playlist, 0)
print(total_playtime)

numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
# list comprehension filters the even numbers
even_nums = [num for num in numbers if num % 2 == 0 ]
print(even_nums)
