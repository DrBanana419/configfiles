nterms=int(input("Number of terms: "))
n1=0
n2=1
dummyvar=0
while dummyvar<nterms:
    nth=n2+n1
    n1=n2
    n2=nth
    dummyvar=dummyvar+1
    print((dummyvar,n1),",")
