import sys

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(0, m):
    if b[i] not in a:
        print("No")
        sys.exit()
    else:
        a.remove(b[i])

print("Yes")
    