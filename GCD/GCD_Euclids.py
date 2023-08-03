def gcd(x,y):
    if x<y:
        (x,y)=(y,x)
    if x%y==0:
        return(y)
    else:
        diff= x-y
        return(gcd(max(y,diff),min(y,diff)))
a = gcd(50,75)
print(a)