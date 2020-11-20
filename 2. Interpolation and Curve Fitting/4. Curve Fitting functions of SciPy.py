# Linear Regression

from scipy.stats import linregress
X = [3, 4, 5, 6, 7, 8]
Y = [0, 7, 17, 26, 35, 45]

L = linregress(X,Y)
print('linregress(X,Y) =', L, end='\n\n')

a0 = L.intercept
a1 = L.slope
print('y = linregress(X,Y).intercept + linregress(X,Y).slope x')
print('y = %f %+f x' % (a0, a1), end='\n\n')

# Polynomial Regression

from scipy.optimize import curve_fit
X = [0, 1, 2, 3, 4, 5]
Y = [2, 8, 14, 28, 39, 62]

# For Quadratic Polynomial
f = lambda x, a0, a1, a2: a0 + a1*x + a2*x**2

a,_ = curve_fit(f, X, Y)                # a,_ neglects the 2nd array 
print('a,_ = curve_fit(f, X, Y)')       # of absolute differences
print('y = a[0] + a[1] x + a[2] x^2')
print('y = %f %+f x %+f x^2' %(a[0],a[1],a[2]), end='\n\n')

# For Cubic Polynomial
f = lambda x, a0, a1, a2, a3: a0 + a1*x + a2*x**2 + a3*x**3

a,_ = curve_fit(f, X, Y)
print('a,_ = curve_fit(f, X, Y)')
print('y = a[0] + a[1] x + a[2] x^2 + a[3] x^3')
print('y = %f %+f x %+f x^2 %+f x^3' %(a[0],a[1],a[2],a[3]), end='\n\n')
