from numpy import array, zeros

'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Taking user input ~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    try:
        N = int(input("Enter the Number of Equations: "))
        if N > 0: break
        else: print("Number of Equations must be greater than 0")
    except ValueError:
        print("Enter a Natural Number")
        
col, colB = [], []
for i in range(N):
    row = []
    for j in range(N):
        while True:
            try:
                coeff = float(input("Enter Coefficient "+str(j+1)+\
                                    " of Equation "+str(i+1)+": "))
            except ValueError:
                print("Enter a Real Number")
                continue
            else: break
        row.append(coeff)
    col.append(row)
    
    while True:
        try:
            const = float(input("Enter the Constant of Equation "+str(i+1)+": "))
        except ValueError:
                print("Enter a Real Number")
                continue
        else: break
    colB.append(const)

A = array(col, float)
B = array(colB, float)
print()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# System of Equations
'''
A = array([[ 3, -.1, -.2],
           [.1,   7, -.3],
           [.3, -.2,  10]], float)
B = array([7.85, -19.3, 71.4], float)
'''
A = array([[2, 7, -1,  3, 1],
           [2, 3,  4,  1, 7],
           [6, 2, -3, 2, -1],
           [2, 1,  2, -1, 2],
           [3, 4,  1, -2, 1]], float)
B = array([5, 7, 2, 3, 4], float)
'''
A = array([[0, 7, -1,  3, 1],
           [2, 3,  4,  1, 7],
           [6, 2,  0, 2, -1],
           [2, 1,  2,  0, 2],
           [3, 4,  1, -2, 1]], float)
B = array([5, 7, 2, 3, 4], float)
'''

N = len(B)

# Coincident or Parallel Equations  # a1 x + b1 y = c1       a2 x + b2 y = c2
for i in range(N-1):
    ratioA = A[i,:] / A[i+1,:]      # A[0,col]/A[1,col]        [a1/a2, b1/b2]
    ratioB = B[i] / B[i+1]          # B[0] / B[1]               c1/c2

    if all(ratioA == ratioA[0]):    # a1/a2 = b1/b2             Conditions of
        if ratioB == ratioA[0]:     # a1/a2 = b1/b2  = c1/c2    coincident
            print("Two or More Equations are Coincident")
        else:                       # a1/a2 = b1/b2 != c1/c2    parallel
            print("Two or More Equations are Parallel")
        raise SystemExit            # else: a1/a2 != b1/b2      intersect


# Elimination:                      # k = 1 to n-1
for k in range(N-1):                # k = 0 to N-2  # Index starts from 0
    
    # Partial Pivoting
    if abs(A[k,k]) < 1e-12:         # 0 in the main diagonal
        for i in range(k+1, N):
            if abs(A[i,k]) > abs(A[k,k]):
                A[[k,i]] = A[[i,k]] # A[k,:], A[k+1,:] = A[k+1,:], A[k,:]
                B[[k,i]] = K[[i,k]] # B[k],   B[k+1]   = B[k+1],   B[k]
                break

    for i in range(k+1, N):         # i = k+1 to N-1
        if A[i,k] == 0: continue    # fctr = A[k,k] / 0 will be inf
        
        fctr = A[k,k] / A[i,k]

        for j in range(k, N):       # j = k to N-1
            A[i,j] = A[k,j] - fctr * A[i,j]

        B[i] = B[k] - fctr * B[i]

# Back Substitution:
X = zeros(N, float)
X[N-1] = B[N-1] / A[N-1][N-1]

for i in range(N-2, -1, -1):        # i = N-2 to 0

    sumAX = 0
    for j in range(i+1, N):         # j = i+1 to N-1
        sumAX += A[i,j] * X[j]

    X[i] = (B[i] - sumAX) / A[i,i]  # X[i]=(B[i]-sum(A[i,i+1:]*X[i+1:]))/A[i,i]

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')

'''
  1  2 3 4  b
1│3 -2 5 0│ 2               
2│4  5 8 1│ 4              
3│1  1 2 1│ 5
4│2  7 6 5│ 7               Elimination:

  1  2   3 4    b
1│3 -2   5 0  │ 2           Fixing row 1, multiply from row 2 to 4, col 1 to b
2│3 3.75 6 .75│ 3                      k              i = k+1 to n, j = k to n
3│3  3   2 3  │15    a[1,1]/a[row,1] a[1,1]/a[2,1] a[1,1]/a[3,1] a[1,1]/a[4,1]
4│3 10.5 6 7.5│10.5           fctr = a[k,k]/a[i,k]

  1  2     3  4     b
1│3 -2     5  0  │  2       From fixed row 1, substract row 2 to 4, col 1 to b
2│0 -5.75 -1 -.75│ -1                      k          i = k+1 to n, j = k to n
3│0 -5    -1 -3  │-13       a[i,j] = a[k,j] - fctr * a[i,j]
4│0 -12.5 -4 -7.5│-8.5      b[i]   = b[k]   - fctr * b[i]


│3 -2     5      0  │ 2     Fixing row 2, multiply from row 3 to 4, col 2 to b
│0 -5.75 -1     -.75│-1                k              i = k+1 to n, j = k to n
│0 -5.75 -1.15 -3.45│-14.95 a[2,2]/a[row,2] a[2,2]/a[3,2] a[2,2]/a[4,2]
│0 -5.75 -1.84 -3.45│-3.91  a[k,k]/a[i,k]

│3 -2     5   0  │ 2        From fixed row 2, substract row 3 to 4, col 2 to b
│0 -5.75 -1  -.75│-1                       k          i = k+1 to n, j = k to n
│0  0    .15  2.7│-14.9     a[i,j] = a[k,j] - fctr * a[i,j]
│0  0    .84  2.7│-3.91     b[i]   = b[k]   - fctr * b[i]


│3 -2     5   0  │ 2        Fixing row 3, multiply from row 4 to 4, col 3 to b
│0 -5.75 -1  -.75│-1                   k              i = k+1 to n, j = k to n
│0  0    .15  2.7│-13.95    a[3,3]/a[row,2] a[3,3]/a[4,3]
│0  0    .15 .482│.51964    a[k,k]/a[i,k]

│3 -2     5   0  │ 2        From fixed row 3, substract row 4 to 4, col 3 to b
│0 -5.75 -1  -.75│-1                       k          i = k+1 to n, j = k to n
│0  0    .15  2.7│13.95     a[i,j] = a[k,j] - fctr * a[i,j]
│0  0     0  2.22│13.43     b[i]   = b[k]   - fctr * b[i]

fctr = a[k,k] / a[i,k]
a[i,j] = a[k,j] - fctr * a[i,j]
b[i]   = b[k]   - fctr * b[i]
where fixed row k = 1 to n-1, row below fixed row i = k+1 to n, j = k to n


Back Substitution :                            AX = B
a[1,1]x[1] + a[1,2]x[2] + a[1,3]x[3] + a[1,4]x[4] = b[1]
             a[2,2]x[2] + a[2,3]x[3] + a[2,4]x[4] = b[2]
                          a[3,3]x[3] + a[3,4]x[4] = b[3]
                                       a[4,4]x[4] = b[4]
x[4] =  b[4] / a[4,4] = 6.056
x[n] =  b[n] / a[n,n]

x[3] = (b[3]                             - a[3,4]*x[4]) / a[3,3] = -16
x[2] = (b[2]               - a[2,3]*x[3] - a[2,4]*x[4]) / a[2,2] = 2.167
x[1] = (b[1] - a[1,2]*x[2] - a[1,3]*x[3] - a[1,4]*x[4]) / a[1,1] = 28.78
x[i] = (b[i] - a[i,j]*x[j] - a[i,j]*x[j] - a[i,j]*x[j]) / a[i,i]

x[i] = (b[i] - ∑(a[i,j]*x[j])) / a[i,i]
where i = n-1 to 1, j = i+1 to n

'''
