"""
You are given an n*n 2D matrix that represents an image. Rotate the image by 90 degrees (Clockwise).
[[1, 2, 3],     [[7, 4, 1],
 [4, 5, 6],  =>  [8, 5, 2],
 [7, 8, 9]]      [9, 6, 3]]
"""

x =   [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# STEP 1 - Find the transpose of the array
n = len(x)
for i in range(n):
    for j in range(i,n):
        temp =x[i][j]
        x[i][j] = x[j][i]
        x[j][i] = temp
    print (x)

# STEP 2 - Mirror the matrix
for i in range(n):
    for j in range(n//2):
        temp =x[i][j]
        x[i][j] = x[i][n - 1 - j]
        x[i][n - 1 - j] = temp
