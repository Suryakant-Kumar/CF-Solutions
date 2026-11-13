t = int(input())
s = input()
removal = 0
for i in range(t-1):
    if s[i]==s[i+1]:
        removal += 1
print(removal)
