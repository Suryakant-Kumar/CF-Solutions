n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    count = 5
    while count:
        if a<=b and a<=c:
            a+=1
        elif b<=a and b<=c:
            b+=1
        else:
            c+=1
        count -= 1
    print(a*b*c)
