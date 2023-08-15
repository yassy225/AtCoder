n = int(input())
a = [int(input()) for _ in range(n)]
d = {}
sorted_a = sorted(list(set(a)))
ans = []

for i,v in enumerate(sorted_a):
    d[v] = i

for j in a:
    ans.append(d[j])

for k in ans:
    print(k)