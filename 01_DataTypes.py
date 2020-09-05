x = 3
print(type(x))
print(x)
print(x + 1)
print(x + 1.0)
x = x+1
x += 1
print(x)
y = 2.5
print(y)
y *=2
print(y)

t = True
f = False 
print(type(t))
print(t and f)
print(t or f)
print(not t)
print(t != f)

hello = 'hello'
world = "world"
print(hello)
print(len(hello))
new = hello + world 
print(new)

s = '    aaa '
print(s.strip())

#Python includes several built-in container types: lists, dictionaries, sets, and tuples.
create_list = [3, 1, 2]
print(create_list, create_list[0], create_list[-1])
create_list[2] = 'add'
print(create_list)
create_list.append('bar')
print(create_list)
a = create_list.pop()
print(a, create_list)

nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[:1])
print(nums[:])
print(nums[-1])
print(nums[:-1])

# Unique characters in string 
straa = 'abcdeeeeffgghhiij'
print(set(straa))
vv = set(straa)
print(type(vv))
