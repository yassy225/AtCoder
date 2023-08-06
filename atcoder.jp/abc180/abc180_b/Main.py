import math
import decimal

n = int(input())
x = list(map(int, input().split()))

manhattan=0
euclid: float = 0
chebyshev = 0

#manhattan
for i in x:
    manhattan += abs(i)

#euclid
for i in x:
    euclid += pow(abs(i),2)

#chebyshev
for i in range(len(x)):
    x[i] = abs(x[i])
chebyshev = max(x)

print(manhattan)
print(math.sqrt(euclid))
print(chebyshev)