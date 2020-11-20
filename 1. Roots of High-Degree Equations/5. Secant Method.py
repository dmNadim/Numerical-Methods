def secant(f, x1, x2, tolerance = 1e-6, maxiter = 100):

    for iterations in range(maxiter):
        
        ## x2-x1 / f(x2)-f(x1) = x2-xnew / f(x2)-0 = x1-xnew / f(x1)-0
        # xnew = (f(x2)*x1 - f(x1)*x2) / (f(x2) - f(x1))# same as false position
        xnew = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)       # Secant equation

        if abs(xnew - x2) < tolerance: break

        else:           # (x1,y1) and (x2,y2) are connected to get intersect x3
            x1 = x2     # (x2,y2) and (x3,y3) are connected to get (x4,0)
            x2 = xnew   # So x2 becomes x1, x3 becomes x2 for next iteration
    else:
        raise OverflowError("Maximum number of iterations reached!")

    return xnew, iterations+1


f = lambda x: 2*x**2 - 5*x + 3    # Function from the given equation

x1, x2 = map(float, input("Enter the initial interval (x1 x2): ").split())
# x1 = 0        # The initial guesses               # x1 ≠ x2
# x2 = 2, -2    # don't have to enclose the root    # else ZeroDivisionError

xnew, iterations = secant(f, x1, x2)

print('The Root: %0.5f' % xnew)
print('The Number of Iterations: %d' % iterations)
