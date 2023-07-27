k = int(input())
a,b = map(int, input().split())
i = j = 0
asum = 0
bsum = 0

while a > 0:
    asum += (a % 10) * pow(k,i)
    a //= 10
    i+=1

while b > 0:
    bsum += (b % 10) * pow(k,j)
    b //= 10
    j+=1

print(asum * bsum)