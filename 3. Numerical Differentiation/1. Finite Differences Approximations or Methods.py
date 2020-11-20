f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2

h = 0.05        # Step size, equal differences of x, ∆x
# h = 0.01      # Smaller step size gives less error
x = 0.1         # Find derivatives of f(x) at point x

## xi = x, x[i+1] = x+h, x[i+2] = x+2*h, x[i-2] = x-2*h

# Forward Differences Approximation:
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Forward Differences Approximation:')
print('f\' (', x, ') = %f' % dff1)
print('f\'\'(', x, ') = %f' % dff2)

# Central Differences Approximation:
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h))/h**2
print('Central Differences Approximation:')
print('f\' (', x, ') = %f' % dfc1)
print('f\'\'(', x, ') = %f' % dfc2)

# Backward Differences Approximation:
dfb1 = (f(x) - f(x-h))/h
dfb2 = (f(x) - 2*f(x-h) + f(x-2*h))/h**2
print('Backward Differences Approximation:')
print('f\' (', x, ') = %f' % dfb1)
print('f\'\'(', x, ') = %f' % dfb2)

# Analytical Differentiation:
dfa1 = lambda x: 0.5*x**4 - 0.6*x**2 + 0.1
dfa2 = lambda x: 2.0*x**3 - 1.2*x
print('Analytical Differentiation:')
print('f\' (', x, ') = %f' % dfa1(x))
print('f\'\'(', x, ') = %f' % dfa2(x))


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Plotting the function ~~~~~~~~~~~~~~~~~~~~~~~~~~

from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, legend, grid, show

h = 0.01
X = linspace(0, 1, 11)          # Divides from 0 to 1 into 11 points

# Central Differences Approximation:
DFC1 = (f(X+h) - f(X-h))/(2*h)
DFC2 = (f(X+h) - 2*f(X) + f(X-h))/h**2

# pyplot.
plot(X,f(X),'-k', X,DFC1,'--b', X,DFC2,'-.r')
xlabel('x')
ylabel('y, y\', y\'\'')
legend(['f(x)', 'f\'(x)', 'f\'\'(x)'])
grid()
show()


"""
f'(x) = df(x)/dx = lim x→0 (∆f(x)/∆x)
f'(x) ≈ (f(x+∆x)-f(x))/∆x 
f'(xi) ≈ (f(x[i+1])-f(xi))/h    where x = xi, x+∆x = x[i+1], ∆x = h

Taylor's series expansion of f(x):
f(x) = f(a) + f'(a)/1! (x-a) + f''(a)/2! (x-a)^2 + f'''(a)/3! (x-a)^3 + ...

The expansion of f(x[i+1]) will be: x = x[i+1], a = xi, x-a = x[i+1]-xi = h
f(x[i+1]) = f(xi) + f'(xi).h + f''(xi).h^2 / 2! + f'''(xi).h^3 / 3! + ...
f'(xi) = (f(x[i+1]) - f(xi))/h - f''(xi).h / 2! - f'''(xi).h^2 / 3! + ...
By omitting the terms containing second and higher derivatives:
f'(xi) = (f(x[i+1]) - f(xi))/h + O(h) ; O(h) is the error from truncation

(a) Forward Finite Differences:     Error O(h)
f'   (xi) = (f(x[i+1]) - f(xi))/h
f''  (xi) = (f(x[i+2]) - 2f(x[i+1]) + f(xi))/h^2
f''' (xi) = (f(x[i+3]) - 3f(x[i+2]) + 3f(x[i+1]) - f(xi))/h^3
f''''(xi) = (f(x[i+4]) - 4f(x[i+3]) + 6f(x[i+2]) - 4f(x[i+1]) + f(xi))/h^4

(b) Central Finite Differences:     Error O(h^2)
f'   (xi) = (f(x[i+1]) - f(x[i-1]))/2h
f''  (xi) = (f(x[i+2]) - 2f(xi) + f(x[i-1]))/h^2
f''' (xi) = (f(x[i+2]) - 2f(x[i+1]) + 2f(x[i-1]) - f(x[i-2]))/2h^3
f''''(xi) = (f(x[i+2]) - 4f(x[i+1]) + 6f(xi) - 4f(x[i-1]) + f(x[i-2]))/h^4

(c) Backward Finite Differences:    Error O(h)
f'   (xi) = (f(xi) - f(x[i-1]))/h
f''  (xi) = (f(xi) - 2f(x[i-1]) + f(x[i-2]))/h^2
f''' (xi) = (f(xi) - 3f(x[i-1]) + 3f(x[i-2]) - f(x[i-3]))/h^3
f''''(xi) = (f(xi) - 4f(x[i-1]) + 6f(x[i-2]) - 4f(x[i-3]) + f(x[i-4]))/h^4

"""
