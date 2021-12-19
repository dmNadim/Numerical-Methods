from numpy import exp, linspace, empty
f = lambda x: exp(x-2) - 3  # Analytical Solution

dy = lambda x, y: y+3   # Equation to be solved, y' = y+3
x = 2                   # Lower limit, [2
xn = 4                  # Upper limit, 4]
y = -2                  # Initial condition, y(2) = -2

h = 0.1                 # Width of each division, step size
n = int((xn-x)/h)       # Number of divisions of the domain

# Plot Arrays
xp = linspace(x, xn, n+1)   # Divides from x to xn into n+1 points
yp = empty(n+1, float)
yp[0] = y


print('x \t\ty(RK4) \t\ty(Analytical)')   # Header of Output
print('%f \t% f \t% f' % (x, y, f(x)))    # Initial x and y

for i in range(1, n+1):
    K1 = h * dy(x,y)
    K2 = h * dy(x + h/2, y + K1/2)
    K3 = h * dy(x + h/2, y + K2/2)
    K4 = h * dy(x + h, y + K3)
    
    y += 1/6*(K1 + 2*K2 + 2*K3 + K4)    # y(x+h) = y(x) + 1/6(K1+2K2+2K3+K4)
    yp[i] = y
    x += h                              # x for next step, x = x + h
    print('%f \t% f \t% f' % (x, y, f(x)))


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Plotting the function ~~~~~~~~~~~~~~~~~~~~~~~~~~
import matplotlib.pyplot as plt

# pyplot.
plt.plot(xp, yp, 'ro', xp, f(xp))   # Default plot is continuous blue line
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['RK4', 'Analytical'])
plt.show()


"""
Taylor's series can be written as
y(x+h) = y(x) + y'(x)h + y''(x)/2! h^2 + y'''(x)/3! h^3 + ...

Approximate solution of Euler's method is obtained by
trancating the series at the first derivative term
y(x+h) = y(x) + y'(x)h

Including the second, third, and forth derivatives

K1 = h y'(x,y)
K2 = h y'(x + h/2, y + K1/2)
K3 = h y'(x + h/2, y + K2/2)
K4 = h y'(x + h, y + K3)
y(x+h) = y(x) + 1/6 (K1 + 2 K2 + 2 K3 + K4)

The initial condition is the value of y(x) at initial domain x

Find the numerical solution of the following differential equation
over the domain [2,4]: y' = y+3,        y(2) = -2

Analytical Solution: y = e^(x-2) - 3

"""
