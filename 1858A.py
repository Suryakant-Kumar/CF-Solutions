n = int(input())
for i in range(0,n):
    a,b,c = map(int,input().split())
    if a==b:
        if c %2 == 0:
            print("Second")
        else:
            print("First")
    elif a>b:
        print("First") 
    else:
        print("Second")