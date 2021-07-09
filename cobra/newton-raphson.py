print("This is a programme for finding the nth root of a positive number r")
n=float(input("n= "))
r=float(input("r= "))
x1=float(input("Initial guess: "))
var=0
while abs(x1**n-r)>.000000001:
    x1=1/n*((n-1)*x1+r/x1**(n-1))
    var += 1
print("Number of iterations:", var)
print(x1)
