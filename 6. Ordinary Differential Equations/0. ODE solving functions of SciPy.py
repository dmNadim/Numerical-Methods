from scipy.integrate import odeint
from numpy import sin, pi, linspace, arange

# First Order ODE:
dy = lambda y, x: x*y   # Equation to be solved, y' = xy
y0 = 1                  # Initial condition, y(0) = 1
x = linspace(0, 2, 5)   # Divides [0,2] into (2-0)/.5 = 4 (+1 as 0 inc.) points

# Odeint Function
y = odeint(dy, y0, x)

print('odeint(dy, y0, x) =', y, sep='\n', end='\n\n')


# First Order ODE:
dy = lambda y, x: y+3   # Equation to be solved, y' = y+3
y0 = -2                 # Initial condition, y(0) = -2
x = linspace(2, 4, 21)  # Divides [2,4] into (4-2)/.1 = 20 (+1 as 0 inc.) points

# Odeint Function
y = odeint(dy, y0, x)

print('odeint(dy, y0, x) =', y, sep='\n', end='\n\n')


# Second Order ODE:
def  dy(y, x):              # Equation to be solved, y'' = 4*x + 10*sin(x) - y
    y, u  = y
    dydx = [u, 4*x + 10*sin(x) - y]
    return dydx

y0 = [0, 2]                 # Initial conditions, y(π) = 1, u(π) = 2
x = arange(pi, 2*pi, .5)    # Arange [π,2π[ in .5 step size

# Odeint Function
sol = odeint(dy, y0, x)

print('odeint(dy, y0, x) =\n    y \t\ty\'', sol, sep='\n')
