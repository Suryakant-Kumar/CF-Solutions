t = int(input())
hiearchy = {"S":0,"M":1,"L":2}
for _ in range(t):
    a,b = input().split()
    if hiearchy[a[-1]]>hiearchy[b[-1]]:
        print(">")
    elif hiearchy[a[-1]]<hiearchy[b[-1]]:
        print("<")
    else:
        if a[-1]=="S":
            if len(a)>len(b):
                print("<")
            elif len(a)<len(b):
                print(">")
            else:
                print("=")
        else:
            if len(a)>len(b):
                print(">")
            elif len(a)<len(b):
                print("<")
            else:
                print("=")