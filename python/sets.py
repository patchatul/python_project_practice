#Sets are collections of unique items with no duplicates.
#They are unordered collection of distinct elements.
#Each item in a set must be unique

set1 = {2, 5, 10}
set2 = {3, 4, 5}
set1.add(6)
union_set = set1.union(set2)
print("union  ", union_set) #{2,3,4,5,10} 5 not repeat

intersect = set1.intersection(set2) 
print("intersect ", intersect) #{5} repeat num

differ = set1.difference(set2)
print("differ ", differ) #{2, 10} return only 1st set -unshow repeat in set1

