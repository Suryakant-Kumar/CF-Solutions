n,q = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
pre = [0]
for v in p:
    pre.append(pre[-1] + v)
for i in range(q):
    x,y = map(int,input().split())
    discount = pre[n-x+y] - pre[n-x]
    print(discount)

