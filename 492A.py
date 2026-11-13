n = int(input())
i = 1
floorLen = 0
while True:
    floorLen += (i/2)*(2+(i-1))
    if floorLen > n:
        print(i-1)
        break
    i+=1 
