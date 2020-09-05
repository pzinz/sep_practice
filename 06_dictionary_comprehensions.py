# dictionary comprehensions 

nums = [0, 1, 2, 3, 4]
even_num_to_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_num_to_squares)

