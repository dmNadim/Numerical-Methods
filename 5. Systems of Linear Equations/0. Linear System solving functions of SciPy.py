from numpy import array, linalg, dot
from scipy.linalg import lu

# System of Equations
A = array([[3,  -.1, -.2],
           [.1,  7,  -.3],
           [.3, -.2, 10]], float)
B = array([10.3, 33.6, 60.2], float)


# Linalg.Solve Function:

X = linalg.solve(A, B)
print("linalg.solve(A, B) = ", X, end='\n\n')


# Dot and Linalg.inv Function:

X = dot(linalg.inv(A), B)
print("dot(linalg.inv(A), B)", X, end='\n\n')


# Scipy.linalg.lu Function:

P, L, U = lu(A)
print("P, L, U = lu(A)")
print("[P] =\n", P, sep='')
print("[L] =\n", L, sep='')
print("[U] =\n", U, sep='')
