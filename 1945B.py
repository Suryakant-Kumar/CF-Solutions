t = int(input())
for _ in range(t):
    a,b,m = map(int,input().split())
    maxa = (m // a) + 1
    maxb = (m // b) + 1
    print(maxa + maxb)