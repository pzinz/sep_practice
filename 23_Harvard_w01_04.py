def add(a,b):
    mysum = a + b
    return mysum

print(add(4,5))

def add_and_sub(a,b):
    mysum = a + b
    mydiff = a - b
    return (mysum,mydiff)

print(add_and_sub(10,5))

print(add)

newadd = add
print(add(10,5))
print(newadd(3,1))

def modify(mylist):
    mylist[0] *= 10

L = [1,3,5,7,9]
modify(L)
print(L)

def modify(mylist):
    mylist[0] *= 10
    return(mylist)
L = [1, 3, 5, 7, 9]
M = modify(L)
print(M is L)

def interest(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

print(interest([1,2,3,4,5], [3,4,5,6,7]))

import random

def password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstu" + "01234567"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw

print(password(10))

def is_vowel(letter):
    if letter in ["aeiouy"]:
        return(True)
    else:
        return(False)

print(is_vowel("a"))
print(is_vowel(4))

def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return(True)
    else:
        return(False)

print(is_vowel(4))


def factorial(n):
    if n == 0:
        return 1
    else:
        N = 1
        for i in range(1, n+1):
            #N = n * (n-1) * (n-2)
            N = i * (N)
        return(N)

print(factorial(5))