# loops 
d = {'person': 2, 'cow': 4, 'spider': 8}
print(d)
for animal in d:
	legs = d[animal]
	print('A %s has %d legs' % (animal, legs))

# item method to access keys and their corresponding values 

d = {'person': 2, 'cat' : 4, 'dog': 4}
for abc,legs in d.items():
	print('A %s has %d legs' % (abc, legs))


