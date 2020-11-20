from numpy import zeros

X = [0.0, 1.5, 2.8, 4.4, 6.1, 8.0]
Y = [0.0, 0.9, 2.5, 6.6, 7.7, 8.0]

n = len(X)-1    # Degree of polynomial = number of points - 1

print("X =", X)
print("Y =", Y, end='\n\n')

xp = float(input("Find Y for X = "))


## y(x) = a0 + (x-x1)a1 + (x-x1)(x-x2)a2 + ... + (x-x1)(x-x2)...(x-xn)an

## Divided differences procedure to get the a's for n+1 = 4 data points:

## Col:     1        2       3       4
## x1   y11 = Y1                            a0 = y11
## x2   y21 = Y2    y22                     a1 = y22
## x3   y31 = Y3    y32     y33             a2 = y33
## x4   y41 = Y4    y42     y43     y44     a3 = y44    an = y[n+1][n+1]

## yi2     = (yi1 - y11) / (xi - x1) where i = 2,3,4
## yi3     = (yi2 - y22) / (xi - x2) where i =   3,4
## yi4     = (yi3 - y33) / (xi - x3) where i =     4
## yi(j+1) = (yij - yjj) / (xi - xj) where j = 1 to n; i = j+1 to n+1


Dy = zeros((n+1, n+1))  # Dy[6,6] # Dy[0-5, 0-5]       # Index stars from 0
Dy[:,0] = Y     # y11 = Y1, y21 = Y2, y(n+1)1 = Y(n+1) # Dy[i][0] = Y[i]

for j in range(n):
    for i in range(j+1, n+1):
        Dy[i, j+1] = (Dy[i,j] - Dy[j,j]) / (X[i] - X[j])


## Substitution procedure:
## y(x) = y11 + (x-x1)y22 + (x-x1)(x-x2)y33+...+(x-x1)(x-x2)...(x-xn)y[n+1][n+1]

## Index starts from 0
##Dy(x) = y00 + (x-x0)y11 + (x-x0)(x-x1)y22+...+(x-x0)(x-x1)...(x-x[n-1])ynn
##Dy(x) = y00 + sum( prod(x-xj) * y[i+1][i+1] ) where i= 0 to n-1; j= 0 to i


yp = Dy[0,0]                    # Initial summation value, a0, y00
for i in range(n):
    
    xprod = 1                   # Initial product value
    for j in range(i+1):
        xprod *= xp - X[j]      # x[0] to x[i] where i = 0 to n-1

    yp += xprod * Dy[i+1][i+1]  # Dy[1,1] to D[n,n]

##  yp += prod(xp - X[:i+1]) * Dy[i+1][i+1]


print("The Y = %.1f"% yp)
