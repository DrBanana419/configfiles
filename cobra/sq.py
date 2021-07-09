def whole(x):
    if x-int(x) != 0:
        p=int(len(str(x))-1-len(str(int(x))))
        N=int(x*10**p)
    else:
        N=int(x)
    return N
N=float(input("Give: "))
n=whole(N)
strn=str(n)
if len(strn) % 2==0:
    f1=int(strn[0]+strn[1])
else:
    f1=int(strn[0])
v=0
while v**2<f1:
    v=v+1
v=v-1
r=f1-v**2
k=2*v
l=0
#K=(k*10+l)*l
if len(strn) % 2==0:
    passes=int(len(strn)/2)
else:
    passes=int((len(strn)-1)/2+1)
if len(strn)%2==0:
    for i in range(1,passes):

         
        f1=int(strn[2*i]+strn[2*i+1])
        New=r*100+f1
        l=0
        while (k*10+l)*l <New:
           l += 1
        l=l-1
        v=v*10+l
        New2=(k*10+l)*l
        r=New-New2
        k=2*v
else:
    for i in range(1,passes):
        f1=int(strn[2*i-1]+strn[2*i])
        New=r*100+f1
        l=0
        while (k*10+l)*l <New:
           l += 1
        l=l-1
        v=v*10+l
        New2=(k*10+l)*l
        r=New-New2
        k=2*v

epasses=int(input("Extra decimal digits: "))
for i in range (0,epasses):
    New=r*100
    l=0
    while (k*10+l)*l<New:
        l += 1
    l=l-1
    v=v*10+l
    New2=(k*10+l)*l
    r=New-New2
    k=2*v
sq=v/10**epasses
def round(x):
    m=x-int(x)
    if m >= 0.5:
        h=int(x)+1
    else:
        h=int(x)
    return h
ratio=round(n/N)
numzero=len(str(ratio))-1
if numzero % 2==0:
    SQ=sq/(10**(numzero/2))
    print(SQ)
else: 
    SQ=sq/(10**((numzero+1)/2))*3.1622776601
    print(SQ)
    
  


