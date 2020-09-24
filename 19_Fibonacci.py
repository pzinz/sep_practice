def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(sum(fibonacci(10000)))

nums = set([1,1,2,2,3,3,4])
print(len(nums))

y = [x**2 for x in range(5)]
print(y)