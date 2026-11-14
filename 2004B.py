t = int(input())
for _ in range(t):
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    if l==L and r==R:
        gates = abs(l-r)
    elif max(l,L) <= min(r,R):
        if l==L or r==R:
            gates = abs(max(l,L)-min(R,r))+1
        else:
            gates = abs(max(l,L)-min(r,R))+2
    else:
        gates = 1
    print(gates)