dummyvar=0
x=0
y=1
while dummyvar<11:
    x=dummyvar/10
    y=y+(y+x)*.1
    dummyvar += 1
print(y)
