import math

n = int(input())
a = list(map(int, input().split()))
sum = 0

while 0 in a:
    try:
        a.remove(0)
    except ValueError:
        pass

for i in range(len(a)):
    sum += a[i]

print(math.ceil(sum / len(a)))