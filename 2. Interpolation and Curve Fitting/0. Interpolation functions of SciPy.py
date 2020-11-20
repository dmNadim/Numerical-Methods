from scipy.interpolate import interp1d, lagrange

X = [0, 20, 40, 60, 80, 100]
Y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

print("X =", X)
print("Y =", Y, end='\n\n')

# Interp1d Function

f = interp1d(X,Y)                   # Linear Interpolation (default)
print("interp1d(X,Y)(50) =", f(50))
print("interp1d(X,Y)(20) =", f(20), end='\n\n')

f = interp1d(X,Y,'quadratic')       # Quadratic Interpolation
print("interp1d(X,Y,'quadratic')(50) = %.3f" % f(50))
print("interp1d(X,Y,'quadratic')(40) = %.3f" % f(40), end='\n\n')

f = interp1d(X,Y,'cubic')           # Cubic Interpolation
print("interp1d(X,Y,'cubic')(50) = %.3f" % f(50))
print("interp1d(X,Y,'cubic')(60) = %.3f" % f(60), end='\n\n')

# Lagrange Function

L = lagrange(X,Y)                   # Lagrange Interpolation
print("lagrange(X,Y)(50) = %.3f" % L(50))
print("lagrange(X,Y)(80) = %.3f" % L(80), end='\n\n')

print("lagrange(X,Y) =", L, sep='\n')
