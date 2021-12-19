from numpy import array, zeros, sqrt

def decomposition(A):
    N = len(A)
    L = zeros((N,N))    # L = [[0.0] * n for i in xrange(n)]
    U = zeros((N,N))    # U = [[0.0 for x in range(n)] for y in range(n)]

    for j in range(N):                                      # j = 0 to N-1
        
        # Upper Triangular
        U[j,j] = 1                                          # i = j, Diagonal 1

        for i in range(j):                                  # i = 0 to j-1

            if j == 0: break                                # No value for Ui0  
            
            U[i,j] = (A[i,j] - sum(L[i,:i]*U[:i,j]))/L[i,i] # k = 0 to i-1

            # sum(U[k][j] * L[i][k] for k in xrange(i))

        # Lower Triangular
        for i in range(j, N):                                   # i = j to N-1

            L[i,j] = A[i,j] - sum(L[i,:j]*U[:j,j])              # k = 0 to j-1

            # sum(U[k][j] * L[i][k] for k in xrange(j))

    print('LU Decomposition:')
    print('[L] =\n', L, sep='')
    print('[U] =\n', U, sep='', end='\n\n')
    return L, U


def solveLU(A, B):
    L, U = decomposition(A)
    N = len(L)
    
    X = zeros(N)
    Y = zeros(N)

    # Forward Substitution
    for i in range(N):                                      # i = 0 to N-1
        Y[i] = (B[i] - sum(L[i,:i] * Y[:i])) / L[i,i]       # j = 0 to i-1

        # sumj = 0
        # for j in range(i):
        #     sumj += L[i,j] * Y[j]
        # Y[i] = (B[i] - sumj) / L[i,i]

    # Backward Substitution
    for i in range(N-1, -1, -1):                            # i = N-1 to 0
        X[i] = (Y[i] - sum(U[i,i+1:] * X[i+1:]))            # j = i+1 to N-1

        # sumj = 0
        # for j in range(i+1, N):
        #     sumj += U[i,j] * X[j]
        # X[i] = (Y[i] - sumj)

    return X


# System of Equations

A = array([[3,  -.1, -.2],
           [.1,  7,  -.3],
           [.3, -.2, 10]], float)
B = array([10.3, 33.6, 60.2], float)

N = len(A)


X = solveLU(A, B)

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')


'''
Decomposition: [A] = [L][U]   # [L][U] ≠ [U][L]    Not commutative

│a11 a12 a13 ... a1n│   │L11  0   0  ...  0 ││U11 U12 U13 ... U1n│
│a21 a22 a23 ... a2n│   │L21 L22  0  ...  0 ││ 0  U22 U23 ... U2n│
│a31 a32 a33 ... a3n│ = │L31 L32 L33 ...  0 ││ 0   0  U33 ... U3n│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ... Unn│

For Doolittle: Lii = 1  All elements on main diagonal of [L] are 1

│a11 a12 a13 ... a1n│   │L11  0   0  ...  0 ││ 1  U12 U13 ... U1n│
│a21 a22 a23 ... a2n│   │L21 L22  0  ...  0 ││ 0   1  U23 ... U2n│
│a31 a32 a33 ... a3n│ = │L31 L32 L33 ...  0 ││ 0   0   1  ... U3n│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ...  1 │

│a11 a12 a13 ... a1n│
│a21 a22 a23 ... a2n│
│a31 a32 a33 ... a3n│ =
│... ... ... ... ...│
│an1 an2 an3 ... ann│

│L11 L11U12     L11U13            ... L11U1n                      │
│L21 L21U12+L22 L21U13+L22U23     ... L21U1n+L22U2n               │
│L31 L31U12+L32 L31U13+L32U23+L33 ... L31U1n+L32U2n+L33U3n        │
│...      ...             ...     ...             ...             │
│Ln1 Ln1U12+Ln2 Ln1U13+Ln2U23+Ln3 ... Ln1U1n+Ln2U2n+Ln3U3n+...+Lnn│

 Li1 Li1U1j+Li2 Li1U1j+Li2U2j+Li3 ... Li1U1j+Li2U2j+Li3U3j+...+Lnj

 where i = 1 to n, j = 1 to n, k = 1 to j


L11 = a11   U12 = a12 / L11   U13 =  a13 / L11          ...
L21 = a21   L22 = a22-L21U12  U23 = (a23-L21U13)/L22    ...
L31 = a31   L32 = a32-L31U12  L33 =  a33-L31U13-L32U23  ...
Ln1 = an1   Ln2 = an2-Ln1U12  Ln3 =  an3-Ln1U13-Ln2U23  ...

Lij = aij   Lij = aij-Li1U1j  Lij =  aij-Li1U1j-Li2U2j
            Uij = aij / Lii   Uij = (aij-Li1U1j)/Lii

Ujj = 1                       j = 1 to n
Uij = (aij - ∑ Lik*Ukj)/Lii   i = 1 to j-1, k = 1 to i-1
Lij =  aij - ∑ Lik*Ukj        i = j to n,   k = 1 to j-1

No value for Ui1 is implimented by skipping Upper Triangular loop for j == 1 
For U1j there is no ∑ and is implimented by k = 1 to 1-1, not entering k loop
For Li1 there is no ∑ and is implimented by k = 1 to 1-1, not entering k loop


Substitution: [A]{X}={B}    => [L][U]{X}={B}    => [U]{X}={y} and [L]{y}={B}

Forward Substitution: [L]{y}={B}

│L11  0   0  ...  0 ││y1│   │b1│
│L21 L22  0  ...  0 ││y2│   │b2│
│L31 L32 L33 ...  0 ││y3│ = │b3│
│... ... ... ... ...││……│   │……│
│Ln1 Ln2 Ln3 ... Lnn││yn│   │bn│

y1 =  b1 / L11
y2 = (b2 - L21y1) / L22
y3 = (b3 - L31y1 - L32y2) / L33
yn = (bn - Ln1y1 - Ln2y2 - ... - L[n,n-1]y[n-1]) / Lnn

yi = (bi - ∑ Lij*yj) / Lii , i = 1 to n, j = 1 to i-1

For y1 there is no ∑ and is implimented by j = 1 to 1-1, not entering j loop

Backward Substitution: [U]{X}={y}

│U11 U12 U13 ... U1n││x1│   │y1│
│ 0  U22 U23 ... U2n││x2│   │y2│
│ 0   0  U33 ... U3n││x3│ = │y3│
│... ... ... ... ...││……│   │……│
│ 0   0   0  ... Unn││xn│   │yn│

xn =  yn
x3 = (y3                   - U34*x4)
x2 = (y2          - U23*x3 - U24*x4)
x1 = (y1 - U12*x2 - U13*x3 - U14*x4)
xi = (yi - Uij*xj - Uij*xj - Uij*xj)

xi = (yi - ∑ Uij*xj)       , i = n to 1, j = i+1 to n

For xn there is no ∑ and is implimented by j = n+1 to n, not entering j loop

'''
