t  =int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    l.sort()
    if l[0]+1 == l[1] and l[0]+2 == l[2]:
        print("YES")
    else:
        print("NO")
