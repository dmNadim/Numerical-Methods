from numpy import array, full, empty

# System of Equations
A = array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]], float)
B = array([2, -1, 3, 2], float)

N = len(B)

X = full(N, 1.0, float) # Initial Gusses array([1.0, 1.0, 1.0, 1.0], float)]

for iterations in range(100):
    for i in range(N):

        s = 0
        for j in range(N):
            if j == i: continue
            s += A[i,j]*X[j]

        xnew = - 1/A[i,i] * (s - B[i])
        
        Xdiff = abs(xnew - X[i]) # Saving differences to check covergence later

        X[i] = xnew


    if (Xdiff < 1e-6).all():
        break 

else:
    raise OverflowError("The System does not have Diagonal Dominance")


print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')
print('The Number of Iterations: %d' % (iterations+1))


'''
4x1 +  x2 + 2x3 -  x4 = 2
3x1 + 6x2 -  x3 + 2x4 = -1
2x1 -  x2 + 5x3 - 3x4 = 3
4x1 +  x2 - 3x3 - 8x4 = 2

x1 = - 1/4 ( x2 + 2x3 -  x4 - 2)
x2 = - 1/6 (3x1 -  x3 + 2x4 + 1)
x1 = - 1/5 (2x1 -  x2 - 3x4 - 3)
x2 =   1/8 (4x1 +  x2 - 3x3 - 2)

xnew[i] = - 1/aii (∑ aij*xj - bi)   where i = 1 to n, j = 1 to n and j ≠ i

'''
