from math import sqrt

x = float(input("Enter the initial value: "))
# x = 0         # The initial guess
# x = 2

diff1 = 1e9     # Initial |xnew - x| is taken any higher value e.g., 1×10^9
divergence = 0  # diff in each iteration has to decrease to achieve convergence 
iterations = 0

while True:
    ## 2x**2 - 5x + 3 = 0           # Given equation
    # xnew = (2*x**2 + 3)/5         # Can be rewritten as
    # xnew = sqrt((5*x-3)/2)        # or as
    
    ## 2x**2 - 4x + 1 = 0
    xnew = (1/2 * x**2 + 1/4)
    # xnew = sqrt((4*x-1)/2)

    diff2 = abs(x - xnew)           # Check if divergence case
    if (diff2 > diff1):
        divergence = 1
        break
    diff1 = diff2
    
    iterations += 1
    if abs(xnew - x) < 1e-2:
        break
    x = xnew
    
    
if(divergence == 0):
    print('The Root: %0.5f' % xnew)
    print('The Number of Iterations: %d' % iterations)
else:
    print("Divergence Case")
