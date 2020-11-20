## (y - y1) / (x - x1) = (y2 - y1) / (x2 - x1)
y = lambda x, x1, x2, y1, y2: y1 + (y2-y1) / (x2-x1) * (x-x1)

def interpolation(xp, X, Y):
    if xp < X[0]:
        print("Given x-value is out of range")
        return None

    for i, Xi in enumerate(X):
        if xp < Xi:
            return y(xp, X[i-1], X[i], Y[i-1], Y[i])
    else:
        print("Given x-value is out of range")

time = [0, 20, 40, 60, 80, 100]
temp = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

print("time =", time)
print("temp =", temp, end='\n\n')

xp = float(input("Find temparture at time = "))

yp = interpolation(xp, time, temp)
print("The temperature =", yp)
