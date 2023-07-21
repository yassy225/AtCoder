import math

p = int(input())
coin = 0

for i in range(10,0,-1):
    if p // math.factorial(i) > 0:
        coin += p // math.factorial(i)
        p %= math.factorial(i)
    else:
        continue

print(coin)