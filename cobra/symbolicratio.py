def bd(x1, x2):
     while x2%x1>0:
           g=x2%x1
           x2=x1
           x1=g
     return x1

def lm(x1, x2):
    return x1*x2/(bd(x1, x2))
n1=int(input("1st numerator: "))
d1=int(input("1st denominator: "))
n2=int(input("2nd numerator: "))
d2=int(input("2nd denominator: "))
sum=n1*lm(d1, d2)/d1+n2*lm(d1, d2)/d2
print(n1,"/",d1,"+",n2,"/",d2,"=",sum,"/",lm(d1, d2))
if bd(sum, lm(d1,d2)) != 1:
    denominator=lm(d1, d2)/bd(sum, lm(d1,d2))
    sum=sum/bd(sum, lm(d1,d2))
print(sum,"/",denominator)
if sum>denominator:
    w=int(sum/denominator)
    p=w*denominator
    r=sum-p
    print(w,"+",r,"/",denominator)
print(w+r/denominator)
