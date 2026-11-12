t = int(input())
for _ in range(t):
    x = int(input())
    cnty = 0
    i = 1
    while x%i==0:
        cnty += 1
        i += 1

    print(cnty)