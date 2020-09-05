import numpy as np

#Create 3 x 4 array 
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(a)

#slicing 
#slice from row 3 and column 2 and 3
b = a[2:, 1:3]
print(b)

#slice all row and column 2 and 3
print(a[:, 1:3])

#slide row 1 and 2 and all colums 
print(a[3:, :])

print(a[2:, :])

print(a[0,1])

#replace 
a[0,0] = 77
print(a[0,0])
print(a)

row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)


