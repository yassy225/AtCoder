n,x = map(int, input().split())
l = list(map(int, input().split()))
d = [0]
count = 1

for i in range(1,n+1):
    if x >= (d[i-1] + l[i-1]):
        count+=1
    d.append(d[i-1] + l[i-1])

print(count)