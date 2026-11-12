x = int(input())

for i in range(x):
    n = int(input())
    m = map(int,input().split())
    zc = n - sum(m)
    if sum(m)>=zc:   
        print("Bessie")
    else:
        print("Elsie")
        