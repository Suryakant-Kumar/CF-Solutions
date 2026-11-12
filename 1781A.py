n = int(input())
for i in range(n):
    w,d,h = map(int,input().split())
    a,b,f,g = map(int,input().split())
    length_w = 0
    length_d = 0

    length_w = min(a+f,(w-a)+(w-f))
    length_w += h
    length_w += max(b,g) - min(b,g)

    length_d = min(b+g,(d-b)+(d-g))
    length_d += h
    length_d += max(a,f) - min(a,f)

    print(min(length_d,length_w))