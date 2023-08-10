import sys

a,b = map(int, input().split())
s = list(input())

for i in range(a):
    if not s[i].isdecimal():
        print("No")
        sys.exit()

if s[a] != '-':
    print("No")
    sys.exit()

for i in range(a+1,a+b+1):
    if not s[i].isdecimal():
        print("No")
        sys.exit()

print("Yes")