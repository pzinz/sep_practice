# Static typing mean that the type checking is performed during compile time

# dynamic typing means that the type checking is performed at run time

# Varible, objects and references
# x = 3 ; Python will first create the object 3 and then create the variable X and then finally reference x -> 3

# list defined as followed
l1 = [2,3,4]
print(type(l1))
l2 = l1
print(type(l2))
l1[0] = 24
print(l1)
print(l2)

# Each object in python has a type, value and identity
L = [1,2,3]
M = [1,2,3]
print(L == M)

print(L is M) # Check whether L is the same object as M
# Above will return False

print('ID of L is:', id(L))
print("ID of M", id(M))

print(id(L) == id(M))

# Mutuable objects can be identical in contents yet be different objects
M = list(L)
print(M is L)

M = L[:]
print(M)

aa = 3
bb = aa
bb = bb - 1
print(aa)

LL = [2,3,4]
M1 = LL
M2 = LL[:]
print(M1 is M2)

# COPIES

# shallow copy
# deep copy
import copy
a = [1,[2]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(b is c)
print(b is a)

print("----------")
print(True or False)
if False:
    print("False")
elif True:
    print("True")
else:
    print("Finally")

print("============")

for x in range(10):
    print(x)

age = {}
print(type(age))
age = dict()
print(type(age))
age = {"Tim": 29, "Jim": 31, "Pam": 27, "Sam": 39}
age["Tom"] = 50
age["Nick"] = 33
names = age.keys()
print(names)
print(age)

for name in names:
    print(name)

print(age.keys())

for name in age.keys():
    print(name,age[name])

for name in sorted(age,reverse=True):
    print(name,age[name])

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if(bears[bear] == "friendly"):
        print("Hello, "+bear+" bear!")
    else:
        print("odd")


print("====")
n = 100
number_of_times = 0
while n >= 1:
    n //= 2
    number_of_times += 1
print(number_of_times)

is_prime = True
for i in range(2,n):
    if n%i == 0:
        print(i)
print(is_prime)

numbers = range(10)
squares = []
for num in numbers:
    square = num **2
    squares.append(square)

print(squares)

squares2 = [number ** 2 for number in numbers]
print(squares2)

for i in range(10):
    print(i)

sum(x for x in range(1,10) if x % 2)
print(sum2)