n = int(input())
for i in range(n):
    x = int(input())
    l = list(map(int,input().split()))
    maxsum = 0
    found = False
    oneminus = False
    for i in range(x):
        if l[i] == -1:
            oneminus = True
            if i+1 != x:
                if l[i+1] == -1:
                    maxsum = sum(l) + 4
                    found = True
                    break
                else:
                    continue
    if found == False:
        if oneminus == True:
            maxsum = sum(l)
        else:
            maxsum = sum(l) - 4
    print(maxsum)