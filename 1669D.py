t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 1:
        if s == "W":
            status = "YES"
        else:
            status = "NO"
    else:
        splits = s.split("W")
        for j in splits:
            if j:
                if len(j)==1:
                    status = "NO"
                    break
                elif len(j)>=2:
                    if "B" not in j or "R" not in j:
                        status = "NO"
                        break
                    else:
                        status = "YES"
            else:
                status  ="YES"
    print(status)
    