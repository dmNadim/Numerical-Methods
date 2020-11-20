from numpy import array

def GaussJordan(A, B):
    N = len(B)
    
    # Main Loop                         # k = 1 to n
    for k in range(N):                  # k = 0 to N-1  # Index starts from 0

        # Partial Pivoting
        if abs(A[k,k]) < 1e-12:         # 0 in the main diagonal
            for i in range(k+1, N):
                if abs(A[i,k]) > abs(A[k,k]):
                    A[[k,i]] = A[[i,k]] # A[k,:], A[k+1,:] = A[k+1,:], A[k,:]
                    B[[k,i]] = K[[i,k]] # B[k],   B[k+1]   = B[k+1],   B[k]
                    break

        # Division of the Pivot Row:
        pivot = A[k,k]                  # Storing A[k,k] in another variable
        for j in range(k, N):           # j = k to N-1
            A[k,j] /= pivot             # as A[k,k] will be 1 at j = k and
        B[k] /= pivot                   # divide by 1 won't change rest cols
        
        # Elimination of Other Rows:
        for i in range(N):              # i = 1 to N-1 and i != k
            if i == k or A[i,k] == 0: continue

            fctr = A[i,k]               # Storing A[i,k] in another variable

            for j in range(k, N):       # j = k to N-1
                A[i,j] -= fctr * A[k,j] # as A[i,k] will be 0 at j = k and

            B[i] -= fctr * B[k]         # substract 0 won't change rest cols
            
    return B                            # AX = B => X = B, A identity matrix 

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
# Augmented Matrices

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


X = GaussJordan(A, B)

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')

'''
   1  2   3    b
1│ 3 -.1 -.2│ 7.85               
2│.1  7  -.3│-19.3           
3│.3 -.2  10│ 71.4          

   1  2     3      b
1│ 1 -.033 -.066│ 2.616     Division: (k = 1, j = k to n)
2│.1  7    -.3  │-19.3      a[1,1...3] = a[1,1...3]/a[1,1]  b[1] = b[1]/a[1,1]
3│.3 -.2    10  │ 71.4      a[k,j] = a[k,j]/a[k,k]          b[k] = b[k]/a[k,k]
                                             pivot
   1  2     3      b
1│ 1 -.033 -.066│ 2.616     Elimination: (i = 2, j = k to n)
2│ 0 7.003 -.293│-19.56     a[2,1...3] = a[2,1...3] - a[2,1]*a[1,1...3]
3│.3 -.2    10  │ 71.4      a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[2]=b[2]-a[2,1]*b[1]
                                           fctr          b[i]=b[i]-a[i,k]*b[k]
   1  2     3      b
1│ 1 -.033 -.066│ 2.616     Elimination: (i = 3, j = k to n)
2│ 0 7.003 -.293│-19.56     a[3,1...3] = a[3,1...3] - a[3,1]*a[3,1...3]
3│ 0 -.19  10.02│ 70.62     a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[3]=b[3]-a[3,1]*b[1]
                                           fctr          b[i]=b[i]-a[i,k]*b[k]

│1 -.033 -.066│ 2.616       Division: (k = 2, j = k to n)
│0  1  -.04188│-2.793       a[2,2...3] = a[2,2...3]/a[2,2]  b[2] = b[2]/a[2,2]
│0 -.19  10.02│ 70.62       a[k,j] = a[k,j]/a[k,k]          b[k] = b[k]/a[k,k]

│1  0  -.06806│ 2.523       Elimination: (i = 1, j = k to n)
│0  1  -.04188│-2.793       a[1,2...3] = a[1,2...3] - a[1,2]*a[2,2...3]
│0 -.19  10.02│ 70.62       a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[1]=b[1]-a[1,2]*b[2]
                                                         b[i]=b[i]-a[i,k]*b[k]
│1  0  -.06806│ 2.523       Elimination: (i = 3, j = k to n)
│0  1  -.04188│-2.793       a[3,2...3] = a[3,2...3] - a[3,2]*a[2,2...3]
│0  0   10.012│ 70.84       a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[3]=b[3]-a[3,2]*b[2]
                                                         b[i]=b[i]-a[i,k]*b[k]

│1  0  -.06806│ 2.616       Division: (k = 3, j = k to n)
│0  1  -.04188│-2.793       a[3,3...3] = a[3,3...3]/a[3,3]  b[3] = b[3]/a[3,3]
│0  0   1     │ 7           a[k,j] = a[k,j]/a[k,k]          b[k] = b[k]/a[k,k]

│1  0   0     │ 3           Elimination: (i = 1, j = k to n)
│0  1  -.04188│-2.793       a[1,3...3] = a[1,3...3] - a[1,3]*a[3,3...3]
│0  0   1     │ 7           a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[1]=b[1]-a[1,3]*b[3]
                                                         b[i]=b[i]-a[i,k]*b[k]
│1  0   0     │ 3           Elimination: (i = 2, j = k to n)
│0  1   0     │-2.5         a[2,3...3] = a[2,3...3] - a[2,3]*a[3,3...3]
│0  0   1     │ 7           a[i,j]=a[i,j]-a[i,k]*a[k,j]  b[2]=b[2]-a[2,3]*b[3]
                                                         b[i]=b[i]-a[i,k]*b[k]

Division: (k = 1 to n, j = k to n)
a[k,j] = a[k,j] / a[k,k]
b[k]   = b[k]   / a[k,k]
Elimination: (k = 1 to n, i = 1 to n and i != k, j = k to n)
a[i,j] = a[i,j] - a[i,k] * a[k,j]
b[i]   = b[i]   - a[i,k] * b[k]

'''
