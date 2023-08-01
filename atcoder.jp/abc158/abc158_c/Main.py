import math
import sys

a,b = map(int, input().split())

for i in range(1,1001):
    if (math.floor(i * 0.08) == a) and (math.floor(i * 0.1) == b):
        print(i)
        sys.exit()

print("-1")