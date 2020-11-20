from math import sin, cos

x = float(input("Enter the initial value: "))
# x = 0         # The initial guess
# x = 2

diff1 = 1e9     # Arbitrary value
divergence = 0
iterations = 0

while True:
    ## f(x) = 2x**2 - 5x + 3                # Given equation
    ## f'(x) = 4x - 5                       # First derivative
    xnew = x - (2*x**2 - 5*x + 3)/(4*x - 5) # The Newton-Raphson's Formula
    
    ## f(x) = x**2 + cos(x)**2 - 4x
    ## f'(x) = 2x - 2cos(x)sin(x) - 4
    # xnew = x - (x**2 + cos(x)**2 - 4*x) / (2*x - 2*cos(x)*sin(x) - 4)
    
    # xnew = x - (2*x**3 - 9.5*x + 7.5) / (6*x**2 - 9.5) ## x = -2.5, 1, 1.5

    iterations += 1
    if abs(xnew - x) < 1e-6:
        break
    x = xnew
    
    diff2 = abs(x - xnew)
    if (diff2 > diff1):
        divergence = 1
        break
    diff1 = diff2

if(divergence == 0):
    print('The Root: %0.5f' % xnew)
    print('The Number of Iterations: %d' % iterations)
else:
    print("Divergence Case")
