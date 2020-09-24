import numpy as np

x = np.array([1,2,4])
y = np.array([2,3,4])

print(x.mean())
print(y.mean())

print(x.shape)


import math
print(math.pi)

print(math.sqrt)

print(np.sqrt)

print(math.sqrt(2))
print(np.sqrt(2))

# numpy can do this
print(np.sqrt([2,3,4]))

# math cannot
#print(math.sqrt([2,3,4]))

name = "abc"
print(type(name))

print(dir(name)) #using name of the object

print(dir(str)) # using object type directly

print(14 * 23)

# print(_)

import math

print(math.factorial(3))

import random

print(random.choice([2,44,66]))

print(random.choice(['a','bb','cc',8]))

print(type(True)) # Boolean Object

# three boolean - Or, And, and Not
print(True or False)
print(True and False)

print (-2 < -4)
print (-2 == -4) # Equal to
print(-2 != -2) # Not Equal

print([2,3] == [3,4]) # test whether object have the same value

print([2,3] == [2,3])

# is test whether object have the same identity 
print([2,3] is [2,3]) # If the first object is the same as second list

print(True and not False is True)