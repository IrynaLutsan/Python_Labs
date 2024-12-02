import math 

x = 7.5 
y = 0.
while x <= 10:
    if x <= 8:
          y = (x**2 - 1)**(x - 1)
    elif x > 8 and x <= 9:
        y = 1 / (math.sin(x) + abs(math.cos(x)))
    else:
        y = math.log(math.e**x + 4)
    print("x = ", round(x,3), "\ty = ", round(y,3))

    x += 0.2
