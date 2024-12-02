import math

a = 0.1 
b = 0.5 
h = 0.05
m = 3
d = 0.001 
x = a 
y = 0

while x >= a and x <= b:
    n = 1
    y = 1
    while True:
        M = (m + 0)
        for i in range(1, n):
            M *= (m + i)
        l = (M / math.factorial(n))*x**n
        if l < d:
            break
        y += l
        n += 1
    print("x = ", round(x,2), "\ty= ", round(y,3))
    x += h
    