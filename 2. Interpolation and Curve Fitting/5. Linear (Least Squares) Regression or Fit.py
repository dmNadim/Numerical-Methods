'''
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Taking user input ~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    try:
        N = int(input("Enter the Number of Points: "))
        if N > 1: break
        else: print("Number of Points must be greater than 1")
    except ValueError:
        print("Enter a Natural Number greater than 1")
X, Y = [], []
for i in range(N):
    while True:
        try:
            x = float(input("Enter the X coordinate of the point "+str(i+1)+": "))
        except ValueError:
                print("Enter a Real Number")
                continue
        else: break
    X.append(x)
    while True:
        try:
            y = float(input("Enter the Y coordinate of the point "+str(i+1)+": "))
        except ValueError:
                print("Enter a Real Number")
                continue
        else: break
    Y.append(y)
print()
'''

# X = [0, 1, 2, 3, 4, 5]
# Y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

X = [3, 4, 5, 6, 7, 8]
Y = [0, 7, 17, 26, 35, 45]

N = len(X)  # Number of data points

# ~~~~~~~~~~~~~~~~~~~~~~~~ Method 1: Using for loop ~~~~~~~~~~~~~~~~~~~~~~~~

sumx = sumy = sumx2 = sumxy = 0 # Initial value of summation variables
for i in range(N):
    sumx += X[i]
    sumy += Y[i]
    sumx2 += X[i]**2
    sumxy += X[i]*Y[i]
meanx = sumx / N
meany = sumy / N

a1 = (N*sumxy - sumx*sumy) / (N*sumx2 - sumx**2)
a0 = meany - a1 * meanx

# ~~~~~~~~~~~~~~~~~ Method 2: Using numpy array, sum, mean ~~~~~~~~~~~~~~~~~

from numpy import array, mean

# sum(X**2) requires X to be a numpy array as python list cannot be squared
X = array(X, float)

# a1 = (sum(X*Y) - mean(X)*sum(Y))/(sum(X**2) - N*mean(X)**2)
# a0 = (mean(Y)*sum(X**2) - mean(X)*sum(X*Y))/(sum(X**2) - N*mean(X)**2)

a1 = (N*sum(X*Y) - sum(X)*sum(Y)) / (N*sum(X**2) - sum(X)**2)
a0 = mean(Y) - a1 * mean(X)


print("The straight line equation :")
s = "-" if a1<0 else "+"
a1 = -a1 if a1<0 else a1
print('y = %.3f %s %.3f x' %(a0, s, a1))


'''
y = a0 + a1 x + e    # where a0 = intercept, a1 = slope, y = mx+c
e = y - a0 - a1 x    # e = true value of y ~ approximate value of a0+a1x

Criteria for a best fit:
∑ (ei) = ∑ (yi - a0 - a1 xi)

Sr = ∑ (ei)^2 = ∑ (yi - a0 - a1 xi)^2

∂Sr/∂a0 = -2    ∑ (yi - a0 - a1 xi)
∂Sr/∂a1 = -2 xi ∑ (yi - a0 - a1 xi)

0 = ∑    yi - ∑ a0    - ∑ a1 xi
0 = ∑ xi yi - ∑ a0 xi - ∑ a1 xi^2

(∑ xi) a0 + (∑ xi^2) a1 = ∑ xi yi
     n a0 + (∑ xi  ) a1 = ∑    yi    # ∑ a0 = n a0

Cross Multiplication:
a1 = ( n ∑ xi yi - ∑ xi ∑ yi ) / ( n ∑ xi^2 - (∑ xi)^2 )

a0 = ( ∑ yi - (∑ xi) a1 ) / n
   = mean(y) - a1 mean(x)

or,
a1 = ( n ∑ xi yi - ∑ xi ∑ yi )/n / ( n ∑ xi^2 - (∑ xi)^2 )/n
   = ( ∑ xi yi - mean(x) ∑ yi ) / ( ∑ xi^2 - n mean(x)^2 )
a0 = ( ∑ xi^2 ∑ yi - ∑ xi ∑ xi yi )/n / ( n ∑ xi^2 - (∑ xi)^2 )/n
   = ( mean(y) ∑ xi^2 - mean(x) ∑ xi yi ) / ( ∑ xi^2 - n mean(x)^2 )

'''
