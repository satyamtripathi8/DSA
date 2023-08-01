#Without using list
x,y = map(int, input().split())
for i in range(1, min(x,y)+1):
    if x%i==0 and y%i==0:
        Recent_factor=i
print("GCD: ",Recent_factor)