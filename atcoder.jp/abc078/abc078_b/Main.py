x,y,z = map(int, input().split())
sum = 0

for i in range(1,100000):
    sum = i*y + (i+1)*z
    if sum > x:
        ans = i-1
        break
    
print(ans)