x,y = map(int, input("Enter Numbers to find Their GCD: ").split())
f1=[]
f2=[]
cf=[]
for i in range(1,x+1):
    if x %i==0:
        f1.append(i)

for i in range(1,y+1):
    if y %i==0:
        f2.append(i)

for i in f1:
    for j in f2:
        if i==j:
            cf.append(i)

print("GCD: ",cf[-1])