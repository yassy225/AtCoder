n = int(input())
sumnumber = 0
result = 0
ans=1

for i in range(1, n+1, 1):
    j=i
    while j % 2 == 0:
        j //= 2
        result += 1
    
    if sumnumber < result:
        sumnumber = result
        ans = i
    result = 0

print(ans)