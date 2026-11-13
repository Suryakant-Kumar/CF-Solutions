t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    new_a = ""
    new_b = ""
    for i in range(n):
        if a[i]==b[i]:
            if a[i] == "R":
                new_a+="R"
                new_b+="R"
            else:
                new_a+="-"
                new_b+="-"
        elif a[i] in "GB" and b[i] in "GB":
            new_a+="-"
            new_b+="-"
        else:
            new_a+=a[i]
            new_b+=b[i]
    if new_b == new_a:
        print("YES")
    else:
        print("NO")
                