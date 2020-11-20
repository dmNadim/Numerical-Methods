from math import sin, pi
from scipy.integrate import quad, dblquad, nquad

# Quad Function:

f = lambda x: x*sin(x)  # Equation to be integrated
a = 0                   # Lower limit
b = pi/2                # Upper limit

I,_ = quad(f, a, b)     # Neglects the 2nd return which is estimated abs error

print('I,_ = quad(f, ', a,', %f)' %b, sep='')
print('I   = %f' % I, end='\n\n')

# DblQuad Function:

fn = lambda x, y: x**2 * y + x * y**2   # Equation to be integrated
ax = 1                                  # Lower limit of inner integral
bx = 2                                  # Upper limit of inner integral
ay = -1                                 # Lower limit of outer integral
by = 1                                  # Upper limit of outer integral

I,_ = dblquad(fn, ax, bx, lambda y:ay, lambda y:by)

print('I,_ = dblquad(fn, ', ax, ', ', bx, ', lambda y:', ay, \
      ', lambda y:', by, ')', sep='')
print('I   = %f' % I, end='\n\n')

# NQuad Function:

I,_ = nquad(f, [[0, pi/2]])

print('I,_ = nquad(f, [[0, pi/2]])')
print('I   = %f' % I, end='\n\n')

I,_ = nquad(fn, [[ax, bx], [ay, by]])

print('I,_ = nquad(fn, [[',ax,', ',bx,'], [',ay,', ',by,']])', sep='')
print('I   = %f' % I)
