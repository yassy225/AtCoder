n,x = map(int, input().split())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    if i % 2 != 0:
        a[i] -= 1
    sum += a[i]

if(x >= sum):
    print("Yes")
else:
    print("No")