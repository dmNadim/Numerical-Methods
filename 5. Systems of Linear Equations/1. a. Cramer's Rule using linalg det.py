from numpy import array, linalg

'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Taking user input ~~~~~~~~~~~~~~~~~~~~~~~~~~~
N = int(input("Enter the Number of Equations: "))

col = []
colB = []
for i in range(N):
    row = []
    for j in range(N):
        coeff = float(input("Enter Coefficient "+str(j+1)+\
                            " of Equation "+str(i+1)+": "))
        row.append(coeff)
    col.append(row)

    const = float(input("Enter the Constant of Equation "+str(i+1)+": "))
    colB.append(const)

A = array(col)
B = array(colB)
print()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Augmented Matrices

A = array([[.3, .52, 1],
           [.5, 1, 1.9],
           [.1, .3, .5]], float)
B = array([-.01, .67, -.44], float)

N = len(B)


coeffMatrix = linalg.det(A)         # [D]

# Coincident or Parallel Equations
if abs(coeffMatrix) < 1e-12:        # Singuar Matrix, ZeroDivisionError
    print("Two or More Equations are Coincident or Parallel")
    raise SystemExit


detMatrix = []
for i in range(N):

    C = A.copy()                    # Making a copy to keep A unchanged
    C [:, i] = B                    # Replace i th coloumn of C with B

    Dx = linalg.det(C)              # |Dx|, |Dy|, |Dz|
    detMatrix.append(Dx)            # [Dx, Dy, Dz]

xMatrix = detMatrix / coeffMatrix   # [Dx/D, Dy/D, Dz/D]

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(xMatrix[i], 6), sep='')
