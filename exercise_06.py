# Take in 10 integers from the user and store them in a list. Create a new list with only elements which appear twice. Print both lists.

import collections  #collections module is used to for things like lists, tuples and dict

#hold all ints1

list = []
counter = 1

for i in range(10):
    nums = int(input(f'Enter Integer {counter}: '))
    list.append(nums)
    counter +=1 
    
seen = set()  # find duplicates duplicates
dupes = set(x for x in list if x in seen or seen.add(x))
        
print(list)
print(dupes)
