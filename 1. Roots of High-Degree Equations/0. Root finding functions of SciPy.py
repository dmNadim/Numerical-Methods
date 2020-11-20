from scipy.optimize import newton, bisect, fsolve, root

f = lambda x: 2*x**2 - 5*x + 3

# Newton-Raphson Function
print('newton(f, 0) = %f' % newton(f, 0))
print('newton(f, 2) = %f' % newton(f, 2), end='\n\n')

# Bisection Function
print('bisect(f, 0, 1.3) = %f' % bisect(f, 0, 1.3))
print('bisect(f, 2, 1.3) = %f' % bisect(f, 2, 1.3), end='\n\n')

# FSolve Function
print('fsolve (f, 0) =', fsolve(f, 0))
print('fsolve (f, 2) =', fsolve(f, 2), end='\n\n')

x0 = [-1, 0, 1, 2, 3, 4]
print('           x0 =', x0)
print('fsolve(f, x0) =', fsolve(f, x0), end='\n\n')

# Root Function
print('root(f, 2) =', root(f, 2), sep='\n', end='\n\n')

print('root (f, 0).x =', root(f, 0).x)
print('root (f, 2).x =', root(f, 2).x, end='\n\n')

print('           x0 =', x0)
print('root(f, x0).x =', root(f, x0).x)




# Default print parameters:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
