from numpy import array, zeros, sqrt, linalg

def symmetric(A):
    return (A == A.T).all()
def positiveDefinite(A):            # for i in range(len(matrix)):
    E = linalg.eigvals(A)           #     if E[i] < 0: return False
    return (E >= 0).all()           # return True


def decomposition(A):
    N = len(A)
    L = zeros((N,N))                # L = zeros_like(A)

    for j in range(N):                                      # j = 0 to N-1
        for i in range(j, N):                               # i = j to N-1
            if i == j:
                L[i,j] = sqrt(A[i,j] - sum(L[i,:j]**2))     # k = 0 to j-1
            else:
                L[i,j] = (A[i,j] - sum(L[i,:j]*L[j,:j])) / L[j,j]

    print('Cholesky Decomposition:')
    print('[L] =\n', L, sep='', end='\n\n')
    return L


def solveCholesky(A, B):
    L = decomposition(A)
    U = L.T
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
        X[i] = (Y[i] - sum(U[i,i+1:] * X[i+1:])) / U[i,i]   # j = i+1 to N-1

        # sumj = 0
        # for j in range(i+1, N):
        #     sumj += U[i,j] * X[j]
        # X[i] = (Y[i] - sumj) / U[i,i]

    return X


# Augmented Matrices

A = array([[ 6,  15,  55],
           [15,  55, 225],
           [55, 225, 979]], float)
B = array([-19, -100, -474], float)
'''
A = array([[8,    3.22,  0.8, 0,     4.10],
           [3.22, 7.76, 2.33, 1.91, -1.03],
           [0.8,  2.33, 5.25, 1,     3.02],
           [0,    1.91, 1,    7.5,   1.03],
           [4.1, -1.03, 3.02, 1.03,  6.44]], float)
B = array([9.45, -12.20, 7.78, -8.1, 10.0], float)
'''
N = len(A)

if symmetric(A) and positiveDefinite(A):
    X = solveCholesky(A, B)
    
    print("The Solution of the System:")
    for i in range(N):
        print('X[', i+1, '] = ', round(X[i], 6), sep='')
else:
    print("The System cannot be Solved by Cholesky Decomposition")


'''
Decomposition: [A] = [L][U]   # [L][U] ≠ [U][L]    Not commutative

│a11 a12 a13 ... a1n│   │L11  0   0  ...  0 ││U11 U12 U13 ... U1n│
│a21 a22 a23 ... a2n│   │L21 L22  0  ...  0 ││ 0  U22 U23 ... U2n│
│a31 a32 a33 ... a3n│ = │L31 L32 L33 ...  0 ││ 0   0  U33 ... U3n│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ... Unn│

Conditions of matrix A for Cholesky Decomposition:
1. Symmetric:        A == A.T for all elements  # aij=aji   i,j = 1 to n
2. Positive Definite: All eigenvalues positive  # linalg.eigvals(A) >= 0

For Cholesky: [A] = [L][L]^T  # [U] = [L]^T       Symmetric matrix

│a11 a12 a13 ... a1n│   │L11  0   0  ...  0 ││L11 L12 L13 ... L1n│
│a21 a22 a23 ... a2n│   │L21 L22  0  ...  0 ││ 0  L22 L23 ... L2n│
│a31 a32 a33 ... a3n│ = │L31 L32 L33 ...  0 ││ 0   0  L33 ... L3n│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ... Lnn│

│a11 a21 a31 ... an1│   │L11  0   0  ...  0 ││L11 L21 L31 ... Ln1│
│a21 a22 a32 ... an2│   │L21 L22  0  ...  0 ││ 0  L22 L32 ... Ln2│
│a31 a32 a33 ... an3│ = │L31 L32 L33 ...  0 ││ 0   0  L33 ... Ln3│
│... ... ... ... ...│   │... ... ... ... ...││... ... ... ... ...│
│an1 an2 an3 ... ann│   │Ln1 Ln2 Ln3 ... Lnn││ 0   0   0  ... Lnn│

│a11       symmetric│
│a21 a22            │
│a31 a32 a33        │ =
│... ... ... ...    │
│an1 an2 an3 ... ann│

│L11^2                                                           symmetric│
│L11L21  L21^2+L22^2                                                      │
│L11L21 L31L21+L32L22  L31^2+L32^2+L33^2                                  │
│ ...        ...             ...           ...                            │
│L11Ln1 Ln1L21+Ln2L22 Ln1L31+Ln2L32+Ln3L33 ... Ln1^2+Ln2^2+Ln3^2+...+Lnn^2│

L11 = √(a11)
L21 = a21/L11   L22 = √(a22-L21^2)
L31 = a31/L11   L32 = (a32-L31L21)/L22   L32 = √(a33-L31^2-L32^2)
    ...             ...                     ...
Ln1 = an1/L11   Ln2 = (an2-Ln1L21)/L22   Ln3 = (an3 - Ln1L31 - Ln2L32) / L33
                                         Lnn = √(ann - Ln1^2 - Ln2^2 - Ln3^2)

Lij = √(aij - ∑ Lik^2)         , i = j, j = 1 to n, i = j to n, k = 1 to j-1
Lij =  (aij - ∑ Lik*Ljk) / Ljj , i ≠ j, j = 1 to n, i = j to n, k = 1 to j-1

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

xn =  yn / Unn
x3 = (y3                   - U34*x4) / U33
x2 = (y2          - U23*x3 - U24*x4) / U22
x1 = (y1 - U12*x2 - U13*x3 - U14*x4) / U11
xi = (yi - Uij*xj - Uij*xj - Uij*xj) / Uii

xi = (yi - ∑ Uij*xj) / Uii , i = n to 1, j = i+1 to n

For xn there is no ∑ and is implimented by j = n+1 to n, not entering j loop

'''
