from math import sin, cos, pi
f = lambda x: 9*pi*cos(x) + 7*sin(x) + 4*x - 5*x*cos(x) # Analytical Solution
df = lambda x: -9*pi*sin(x) + 7*cos(x) + 4 - 5*(cos(x)-x*sin(x))

dy = lambda x,y,u: u                    # 1st Derivative, y' = u
du = lambda x,y,u: 4*x + 10*sin(x) - y  # 2nd Derivative, u' = 4x+10sin(x)-y
x = pi                                  # Lower limit, [π
xn = 2*pi                               # Upper limit, 2π]
y = 0                                   # Initial condition, y(π) = 0
u = 2                                   # Initial condition, u(π) = 2

h = 0.5                 # Width of each division, step size
# h = 0.1               # Smaller step size gives less error
n = int((xn-x)/h)       # Number of divisions of the domain


print('x \t\ty(RK4) \t\ty\'(RK4) \ty(Exact) \ty\'(Exact)')  # Header of Output
print('%f \t%f \t%f \t%f \t%f' % (x, y, u, f(x), df(x)))    # Initial x and y

for i in range(n):
    L1 = h * du(x,y,u)
    K1 = h * dy(x,y,u)
    L2 = h * du(x + h/2, y + K1/2, u + L1/2)
    K2 = h * dy(x + h/2, y + K1/2, u + L1/2)
    L3 = h * du(x + h/2, y + K2/2, u + L2/2)
    K3 = h * dy(x + h/2, y + K2/2, u + L2/2)
    L4 = h * du(x + h, y + K3, u + L3)
    K4 = h * dy(x + h, y + K3, u + L3)
    
    u += 1/6*(L1 + 2*L2 + 2*L3 + L4)    # u(x+h) = u(x) + 1/6(L1+2L2+2L3+L4)
    y += 1/6*(K1 + 2*K2 + 2*K3 + K4)    # y(x+h) = y(x) + 1/6(K1+2K2+2K3+K4)
    x += h                              # x for next step, x = x + h
    print('%f \t%f \t%f \t%f \t%f' % (x, y, u, f(x), df(x)))


"""
2nd order ODE y'' = f(x,y,y') should be divided into two first order ODE's
y' = u    and  u' = f(x,y,u)

The two equations are solved simultaneously using RK4

L1 = h u'(x,y,u)
K1 = h y'(x,y,u)
L2 = h u'(x + h/2, y + K1/2, u + L1/2)
K2 = h y'(x + h/2, y + K1/2, u + L1/2)
L3 = h u'(x + h/2, y + K2/2, u + L2/2)
K3 = h y'(x + h/2, y + K2/2, u + L2/2)
L4 = h u'(x + h, y + K3, u + L3)
K4 = h y'(x + h, y + K3, u + L3)

u(x+h) = u(x) + 1/6 (L1 + 2 L2 + 2 L3 + L4)
y(x+h) = y(x) + 1/6 (K1 + 2 K2 + 2 K3 + K4)

The initial condition is the value of y(x) at initial domain x

Find the numerical solution of the following differential equation
over the domain [π,2π]: y''+y = 4x+10sin(x),    y(π) = 0, y'(π) = 2

y' = u,             y(π) = 0
u' = 4x+10sin(x)-y, u(π) = 2

Analytical Solution: y = 9π cos(x) + 7sin(x) + 4x - 5x cos(x)

"""
