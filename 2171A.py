x = int(input())
 
for i in range(0,x):
    n = int(input())
    if n % 2 != 0:
        print(0)
    else:
        print((n//4)+1)