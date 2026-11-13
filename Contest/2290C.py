t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    cnt = {}
    for v in h:
        cnt[v] = cnt.get(v, 0) + 1

    mx = max(h)
    keys = sorted(v for v in cnt if v != mx)

    left = keys
    right = [v for v in reversed(keys) if cnt[v] >= 2]

    mid = [mx] * cnt[mx]
    for v in keys:
        used = 2 if cnt[v] >= 2 else 1
        mid.extend([v] * (cnt[v] - used))

    k = len(left) + len(right) + min(cnt[mx], 2)
    print(k)
    print(" ".join(map(str, left + mid + right)))