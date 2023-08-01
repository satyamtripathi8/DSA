# Scanning backwards to get GCD
x,y = map(int, input().split())
i= min(x,y)
while i>0:
    if x%i==0 and y%i==0:
        print("GCD: ",i)
        break
    else:
        i=i-1