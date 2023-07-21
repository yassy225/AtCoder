a,b,c,d = map(int, input().split())
takahashi = 0
aoki = 0

while c > 0:
    c -= b
    takahashi += 1

while a > 0:
    a -= d
    aoki += 1

if takahashi > aoki:
    print("No")
else:
    print("Yes")