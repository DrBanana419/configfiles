def squareroot(x):
    import random
    import math
    g=random.randint(int(x-x**2),int(x+x**2))
    while abs(x-g**2)>0.00000000000001:
        g=(g+x/g)/2
    return abs(g)
print("This programme gives you the sum of a number and its square root, and then takes the square root of the sum")
v=float(input("Number: "))
print(squareroot(v+squareroot(v)))
