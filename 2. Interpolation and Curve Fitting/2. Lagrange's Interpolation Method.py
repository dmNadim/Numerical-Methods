X = [0, 20, 40, 60, 80, 100]
Y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

n = len(X)-1    # Degree of polynomial = number of points - 1

print("X =", X)
print("Y =", Y, end='\n\n')

xp = float(input("Find Y for X = "))


# For degree of polynomial 3, number of points n+1 = 4:
# L[1] = (x-x2)/(x1-x2) * (x-x3)/(x1-x3) * (x-x4)/(x1-x4)
# L[2] = (x-x1)/(x2-x1) * (x-x3)/(x2-x3) * (x-x4)/(x2-x4)
# L[3] = (x-x1)/(x3-x1) * (x-x2)/(x3-x2) * (x-x4)/(x3-x4)
# L[4] = (x-x1)/(x4-x1) * (x-x2)/(x4-x2) * (x-x3)/(x4-x3)

# L[i] *= (x-xj)/(xi-xj) where i, j = 1 to n+1 and j != i
# y    += Y[i]*L[i]      where i    = 1 to n+1
                         # List index 0 to n


# ~~~~~~~~~~~~~~~~~~~~~~~~ Method 1: Using for loop ~~~~~~~~~~~~~~~~~~~~~~~~

yp = 0                          # Initial summation value
for i in range(n+1):
    
    L = 1                       # Initial product value
    for j in range(n+1):
        if j == i: continue     # j == i gives ZeroDivisionError
        L *= (xp - X[j]) / (X[i] - X[j])
        
    yp += Y[i]*L


# ~~~~~~~~~~~~~~~~~~~ Method 2: Using numpy array, prod ~~~~~~~~~~~~~~~~~~~~

from numpy import array, prod

X = array(X, float)
Y = array(Y, float)

yp = 0
for Xi, Yi in zip(X, Y):
    yp += Yi * prod((xp - X[X != Xi]) / (Xi - X[X != Xi]))


print("The Y = %.1f"% yp)


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Plotting the function ~~~~~~~~~~~~~~~~~~~~~~~~~~

from numpy import append, linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show

xplot = linspace(X[0], X[-1])   # Divides from 1st to last element of X
yplot = array([], float)        # into 50 points

for xp1 in xplot:

    yp1 = 0
    for Xi, Yi in zip(X, Y):
        yp1 += Yi * prod((xp1 - X[X != Xi]) / (Xi - X[X != Xi]))

    yplot = append(yplot, yp1)

# pyplot.
plot(X, Y, 'ro', xplot, yplot, 'b-', xp, yp, 'bo')
xlabel('x')
ylabel('y')
show()
