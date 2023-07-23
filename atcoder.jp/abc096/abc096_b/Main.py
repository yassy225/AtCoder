a = list(map(int, input().split()))
k = int(input())

a.sort(reverse=True)

for i in range(k):
    a[0] *= 2

print(sum(a))