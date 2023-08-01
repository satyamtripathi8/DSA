#Without using multiple loops and list
x,y = map(int, input().split())
cf=[]
for i in range(1, min(x,y)+1):
    if x%i==0 and y%i==0:
        cf.append(i)
print("GCD: ",cf[-1])