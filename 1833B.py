t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    order = sorted(range(n), key=lambda i: a[i])

    res = [0] * n
    for j in range(n):
        res[order[j]] = b[j]
    print(*res)