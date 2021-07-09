import random
import math
x=float(input("Give number: "))
g=random.randint(int(x-x**2),int(x+x**2))
while abs(x-g**2)>0.00000000000001:
    g=(g+x/g)/2
    print(abs(g))
