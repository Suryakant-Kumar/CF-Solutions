t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    nlist = list(map(int,input().split()))
    score = 0
    hm = [0] * (n+1)
    for i in nlist:
        hm[i] += 1
    for i in range(n):
        if hm[nlist[i]]>0:
            hm[nlist[i]] -= 1
            if 1 <= k - nlist[i] <= n and hm[k-nlist[i]] > 0:
                score +=1
                hm[k-nlist[i]]-=1
    print(score)

        