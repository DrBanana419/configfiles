sum=0
x=int(input("Start: "))
y=int(input("End: "))
for i in range(x,y):
    sum=sum + 1/i
    print(i,1/i)
print("Sum:", sum)

