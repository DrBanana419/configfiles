x=0
y=1
dummyvar=0
while dummyvar<11:
    x=dummyvar/10
    y=y+y*0.1
    print((x,y),",")
    dummyvar=dummyvar+1
print(y)
