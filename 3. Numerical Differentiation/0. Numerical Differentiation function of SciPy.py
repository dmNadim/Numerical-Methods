from scipy.misc import derivative

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2

dx = 0.01       # Step size, equal differences of x, ∆x
# dx = 0.001    # Smaller step size gives less error
x0 = 0.1        # Find derivatives of f(x) at point x

# Derivative Function:
y1 = derivative(f, x0, dx, 1)   # n = 1 for 1st derivative
y2 = derivative(f, x0, dx, 2)   # n = 2 for 2nd derivative

print('derivative(f, ', x0,', ', dx,', 1) = %f' % y1, sep='')
print('derivative(f, ', x0,', ', dx,', 2) = %f' % y2, sep='')


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Plotting the function ~~~~~~~~~~~~~~~~~~~~~~~~~~

from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, legend, grid, show

X = linspace(-1, 1)             # Divides from -1 to 1 into 50 points

# Central Differences Approximation :
DFC1 = derivative(f, X, dx, 1)
DFC2 = derivative(f, X, dx, 2)

# pyplot.
plot(X,f(X),'-k', X,DFC1,'--b', X,DFC2,'-.r')
xlabel('x')
ylabel('y, y\', y\'\'')
legend(['f(x)', 'f\'(x)', 'f\'\'(x)'])
grid()
show()
