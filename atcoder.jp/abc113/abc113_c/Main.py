N,M = map(int, input().split())
D = [[] for i in range(N)]

for i in range(M):
    p,y = map(int, input().split())
    D[p-1].append((y, i))

ans = [None]*M

for i,d in enumerate(D):
    d.sort()
    for k,(y,j) in enumerate(d):
        ans[j] = str(i+1).zfill(6) + str(k+1).zfill(6)

print(*ans, sep="\n")