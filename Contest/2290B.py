t = int(input())
for _ in range(t):
    l = int(input())
    s = input()
    color = "R"
    switch = 0
    for i in s:
        auto = False
        if i != color:
            switch += 1
            if color == "R":
                color = "B"
            else:
                color = "R"
            auto = True
        else:
            if color == "R":
                color = "B"
            else:
                color = "R"
        if auto:
            if color == "R":
                color = "B"
            else:
                color = "R"

    print(switch)