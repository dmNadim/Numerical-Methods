from numpy import array, delete
# delete(arr, obj = row/col no. or slice, axis = 0 for row/1 for col)

def smaller_matrix(matrix, j):
    new_matrix = matrix.copy()              # Keeping original matrix unchanged
    new_matrix = delete(new_matrix, 0, 0)   # remove cofactor row 0
    new_matrix = delete(new_matrix, j, 1)   # remove cofactor coloumn j
    return new_matrix

def determinant(matrix):
    num_rows = len(matrix)
    
    for row in matrix:
        if len(row) != num_rows:
            print("\nNot a Square Matrix")
            return None
    
    if num_rows == 1:
        return matrix[0][0]
    
    elif num_rows == 2:
        base_determinant = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return base_determinant
    else:   
        answer = 0
        num_coloumns = num_rows                         # Cofactor Expansion on
        for j in range(num_coloumns):                   # row 0, col j -1^(0+j)
            cofactor = (-1) ** j * matrix[0][j] \
            * determinant(smaller_matrix(matrix, j))    # Recursive fn finds
            answer += cofactor                          # det of smaller matrix 
        return answer

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

A = array([[.3, .52, 1],
           [.5, 1, 1.9],
           [.1, .3, .5]], float)
B = array([-.01, .67, -.44], float)

N = len(B)


coeffMatrix = determinant(A)        # [D]

# Coincident or Parallel Equations
if abs(coeffMatrix) < 1e-12:        # Singuar Matrix, ZeroDivisionError
    print("Two or More Equations are Coincident or Parallel")
    raise SystemExit

detMatrix = []
for j in range(N):

    C = A.copy()                    # Making a copy to keep A unchanged 
    C [:, j] = B                    # Replace i th coloumn of C with B

    Dx = determinant(C)             # |Dx|, |Dy|, |Dz|
    detMatrix.append(Dx)            # [Dx, Dy, Dz]

xMatrix = detMatrix / coeffMatrix   # [Dx/D, Dy/D, Dz/D]


print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(xMatrix[i], 6), sep='')
