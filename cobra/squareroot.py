def whole(x):
    if x-int(x) != 0:
        p=len(str(x))-1-len(str(int(x)))
        N=x*10**p
    else:
        N=float(x)
    return N
n=float(input("Give: "))
whn=whole(n)
def two(v, w):
    whv=whole(v)
    p1=2*w
    n1=int(whv/10**p1)
    return n1
60589669
z=two(60589669, (len(str(60589669.0))-2)/2-1)
print(z)
z1=two(60589669, (len(str(60589669.0))-2)/2-2)
#z3=z1/10**(len(str(z1)))
z2=len(str(z1))-len(str(z))
print(z1-z*10**(z2))
z3=two(60589669, (len(str(60589669.0))-2)/2-3)
z4=int(z3/10**2)
z5=z4*10**2
z6=z3-z5
print(z6)
z7=two(60589669, (len(str(60589669.0))-2)/2-4)
z8=z7/10**2
z9=int(z8)
z10=z9*10**2
z11=z7-z10
print(z11)


