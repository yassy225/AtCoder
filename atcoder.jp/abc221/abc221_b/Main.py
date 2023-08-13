import sys
s = list(input())
t = list(input())
cnt = 0
s2 = s.copy()

if s == t:
    print("Yes")
    sys.exit()

for i in range(len(s)-1):
    tmp = s[i]
    s[i] = s[i+1]
    s[i+1] = tmp
    if s == t:
        print("Yes")
        sys.exit()
    s = s2.copy()

print("No")