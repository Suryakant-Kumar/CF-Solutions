t = int(input())
for _ in range(t):
    a,b,n = map(int,input().split())
    if a == b or n*b<= a:
        shift = 1
        print(shift)
    else:
        shift = 2
        print(shift)
