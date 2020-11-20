## ⌠1  ⌠2
## ⌡-1 ⌡1 (x^2 y + x y^2) dx dy

f = lambda x, y: x**2 * y + x * y**2    # Equation to be integrated
ax = 1                                  # Lower limit of inner integral
bx = 2                                  # Upper limit of inner integral
ay = -1                                 # Lower limit of outer integral
by = 1                                  # Upper limit of outer integral

nx = 10                 # Number of divisions of inner integral
ny = 10                 # Number of divisions of outer integral
hx = (bx - ax) / nx     # Width of each division of inner integral
hy = (by - ay) / ny     # Width of each division of outer integral

## Using Simpson's 1/3 rule for both integrations:
## I = hx*hy/9 {f[0] + 4*4f[1] + 2*2f[2] + 4*4f[3] + 2*2f[4] + ... + 1*4ƒ(1,0)
##                 + 2*2f[n-4] + 4*4f[n-3] + 2*2f[n-2] + 4*4f[n-1] + f[n]}
## I = hx*hy/9 [p*q * f(ax + j*hx, ay + i*hy)]
## where i = 0 to ny+1 and j = 0 to nx+1

S = 0
for i in range(ny+1):
    if i == 0 or i == ny: p = 1         #  f[0],  f[n]
    elif i % 2 == 1: p = 4              # 4f[1], 4f[3], 4f[n-3], 4f[n-1]
    else: p = 2                         # 2f[2], 2f[4], 2f[n-4], 2f[n-2]

    for j in range(nx+1):
        if j == 0 or j == nx: q = 1     ## For Simpson's 3/8 rule:
        elif j % 2 == 1: q = 4          ## j%3 == 1 or j%3 == 2: q = 3
        else: q = 2

        S += p*q * f(ax + j*hx, ay + i*hy)
        
I = hx*hy/9 * S

print("Integral of the equation, I = %f" % I)


'''
The extended form of the Simpson's 1/3 rule:
I = 1/3 h {f[0] + 4f[1] + 2f[2] + 4f[3] + 2f[4] + ... +
                2f[n-4] + 4f[n-3] + 2f[n-2] + 4f[n-1] + f[n]}

The extended form of the Simpson's 1/3 rule:
I = 3/8 h {f[0] + 3f[1] + 3f[2] + 2f[3] + 3f[4] + 3f[5] + 2f[6] + ... +
                2f[n-3] + 3f[n-2] + 3f[n-1] + f[n])}
where f = ƒ(x,y)

Number of divisions must be even for Simpson's 1/3 rule
Number of divisions must be multiple of 3 for Simpson's 3/8 rule

ʃʃ ƒ(x,y) dx dy

Final common factor when using Simpson's 1/3 rule for both integrations:
hx/3 * hy/3 = hx*hy/9

Final common factor when using Simpson's 3/8 rule for both integrations:
3hx/8 * 3hy/8 = 9hx*hy/64

Final common factor when using different rule for different integration:
3hx/8 * hy/3 = 3hx*hy/24

Weighing factor of each f term is also multiplied depending on used rule
p*q where p is outer and q is inner weighing factor

'''
