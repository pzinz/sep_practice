# Sequence Object
# list 2. Tuple 3. Range Object

# LIST
# list are sequences of any types of python objects

b = [1, 2, 3]
print(type(b))
print(b)
print(b[2])
print(b[-0])

print(b[-0:0])

# List
# list are any type of python objects
# lists are mutable

numbers = [2, 4, 6, 8]
print(numbers[0])
print(numbers[-1])
print(numbers[-0])
print(numbers[-0] == numbers[0])
print(numbers[-0:0])

numbers.append(10)
print(numbers)

x = [12,14,16]
print(numbers + x)
print(type(numbers + x))

new_numbers = [1,3,5,7,9,11,13]
new_numbers.reverse()
print(new_numbers)

names = ['A', 'Z', 'C', 'B']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

sorted_names = sorted(names)
print(names)
print(sorted_names)
print(len(names))

# TUPLES
# Tuples are immutable sequences so they can't be edited after they've been created
T = (1,3,5,7)
print(T)

print(T + (9 , 10))

# Pack and Unpack Tuples
x = 12.23
y = 7.3

coordinate = (x,y) # Packing a tuple
print(type(coordinate))
print(coordinate)

(x1, y1) = coordinate
print(x1)
print(y1)

tuple_new = [(0,0), (1,1), (2,4), (3,9),(4,16), (5,25), (6,36), (7,49), (8,64), (9,81)]
print(tuple_new)

for (x,y) in tuple_new:
    print(x,y)

for x,y in tuple_new:
    print (x,y)

c = (2,3)
print(type(c))

c = (4)
print(type(c))

c =(5,)
print(type(c))

print(T.count(3))
print(sum(T))

# RANGES
print(range(0,5))

print(list(range(0,5)))
print(type(list(range(0,5))))

print(tuple(range(0,5)))
print(type(tuple(range(0,5))))

print(list(range(1,6)))
print(list(range(1,13,2))) # 2 is the step size over here

# STRINGS
# Strings are immutable sequence of characters

S = "Python"
print(len(S))
print(S[0])
print(S[-1])
#Slicing
print(S[0:3])
print(S[-3:])
print(S[-0:0])

print("y" in S)

print(3 * S)

# Below will thrown an error as the first object is string
#print("string " + 8)

print("string " + str(8))

print(dir(str))

#str.replace?

name = "Tina Fey"
name.replace("T", "t")
print(name)

names = name.split(" ")
print(type(names))
print(names[0])
print(type(names[0]))

print(names[0].upper())

print(names[0].isupper())

print(2 * "2")

print(str(range(10)))

import string
print(string.digits)

x = "125,000"
print(x)
print(x.isdigit())

# SET
# SETS ARE UNordered collection of distinct hashable objects
ids = set()
ids = set([1,2,4,6,7,8,9])
print(len(ids))

ids.add(10)
print(ids)

ids.add(2)
print(ids) # since we already have 2 it won't have any effect

print(ids.pop())
print(ids.pop())

ids = set(range(10))
print(ids)

males = set([1,3,5,6,7])
females = ids - males
print(type(females))

print(females)

everyone = males | females
print(everyone)

print(everyone & set([1,2,3]))

word = "antidisestablishmentarism"

letters = set(word) # returns unique characters from the string
print(letters)

aa = set([1,2,3])
print(aa)
bb = set([2,3,4])
print(bb)

print(aa & bb)
print(aa.intersection(bb))
print(aa | bb)
print(bb - aa)
print(aa ^ bb)
print(bb.difference(aa))

print(aa.issubset(bb))

# DICTIONARY
# DICTIONARY ARE MUTUABLE - contents can be modified
# dictionaries are not sequences and thus do not maintain any left or right order
# dictionary keys are not mutuable
# only mutuable types are allowed as keys 
age = {}
print(type(age))
age = dict()
print(type(age))
age = {"Tim": 29, "Jim": 31, "Pam": 27, "Sam": 39}
print(age["Pam"])

age["Tim"] = age["Tim"] + 1
age["Tim"] += 1

print(age["Tim"])

# VIEW OBJECT - dynamic view of the keys or values in the dictionary
names = age.keys()
print(type(names))

#add key to dictionary
age["Tom"] = 50
print(names)

print(age.values())

age["Pritish"] = 33
print(names)
print(age)

print("pritish" in age)
print("Pritish" in age)

#print(age[1]) # there is no key of 1 in dictionary


