from math import exp
f = lambda x: exp(x**2/2)   # Analytical Solution

dy = lambda x, y: x*y   # Equation to be solved, y' = xy
x = 0                   # Lower limit, [0
xn = 2                  # Upper limit, 2]
y = 1                   # Initial condition, y(0) = 1

h = 0.5                 # Width of each division, step size
# h = 0.1               # Smaller step size gives less error
n = int((xn-x)/h)       # Number of divisions of the domain


print('x \t\ty(RK2) \t\ty(Analytical)') # Header of Output
print('%f \t%f \t%f' % (x, y, f(x)))    # Initial x and y

for i in range(n):
    K1 = h * dy(x,y)
    K2 = h * dy(x + h/2, y + K1/2)
    
    y += K2             # y for next step, y(x+h) = y(x) + K2
    x += h              # x for next step, x = x + h
    print('%f \t%f \t%f' % (x, y, f(x)))


"""
Taylor's series can be written as
y(x+h) = y(x) + y'(x)h + y''(x)/2! h^2 + y'''(x)/3! h^3 + ...

Approximate solution of Euler's method is obtained by
trancating the series at the first derivative term
y(x+h) = y(x) + y'(x)h

Including the second derivative
y(x+h) = y(x) + y'(x + h/2, y + y'(x,y)h/2) h

K1 = h y'(x,y)
K2 = h y'(x + h/2, y + K1/2)
y(x+h) = y(x) + K2

The initial condition is the value of y(x) at initial domain x

Find the numerical solution of the following differential equation
over the domain [0,2]: y' = xy,       y(0) = 1

Analytical Solution: y = e^(x^2/2)

"""
