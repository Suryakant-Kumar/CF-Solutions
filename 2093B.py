t = int(input())
for _ in range(t):
    s = input()
    l = s.split("0")
    nonzero = len("".join(l))
    m = s.rstrip("0")
    rfb = len(s)-len(m)
    print(rfb+nonzero-1)