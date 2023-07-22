N,D = map(int, input().split())
S = [input() for i in range(N)]

cnt = 0
result = 0
ans = 0

for i in range(D):
    for j in range(N):
        if S[j][i] == 'o':
            cnt += 1
    if cnt == N:
        result += 1
    else:
        result = 0
    cnt = 0
    ans = max(ans,result)

print(ans)