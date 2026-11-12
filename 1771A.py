t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    mini = x[0]
    minicount = 0
    maxi = x[0]
    maxicount = 0
    for i in x:
        if mini > i:
            mini = i
            minicount = 1
        elif mini == i:
            minicount+=1
        if maxi < i:
            maxi = i
            maxicount = 1
        elif maxi == i:
            maxicount += 1
    if mini == maxi:
        print(n*(n-1))
    else:
        print(minicount*maxicount*2)
