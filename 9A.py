y,w = map(int,input().split())
m = max(y,w)
available = (6-m)+1
den = 6
i = 2
while i <= 6:
    if available%i==0 and den%i==0:
        available = available // i
        den = den // i
        i=2
    i+=1
print(f"{available}/{den}")