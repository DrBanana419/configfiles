import math
x=0
y=9.99 
dummyvar=0
while dummyvar<2001:
    x=dummyvar/100
    y=y+(-math.sqrt(2*6.673*10**(-11)*5*10**10*(10-y)/(10*y)))*0.01
    print((x,y),",")
    dummyvar += 1
