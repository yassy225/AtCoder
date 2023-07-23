import math
n = int(input())
r = []

for _ in range(n):
    r.append(int(input()))

flg = True
sum = 0

r.sort(reverse=True)

for i in range(n):
    if flg:
        sum += r[i] * r[i]
        flg = False
    else:
        sum -= r[i] * r[i]
        flg = True

print(sum * math.pi)