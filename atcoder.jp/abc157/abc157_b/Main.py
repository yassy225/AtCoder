a = [list(map(int, input().split())) for l in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

#当たっているかを確認
for i in range(len(b)):
    for j in range(3):
        for k in range(3):
            #print("b[i]:", b[i])
            #print("a[j][k]:", a[j][k])
            if b[i] == a[j][k]:
                a[j][k] = 0

#ビンゴ判定
# 横一列
for i in range(3):
    cnt = 0
    for j in range(3):
        cnt += a[i][j]
    if cnt == 0:
        print("Yes")
        exit()

#縦一列
for i in range(3):
    cnt = 0
    for j in range(3):
        cnt += a[j][i]
    if cnt == 0:
        print("Yes")
        exit()

#ななめ
if a[0][0] + a[1][1] + a[2][2] == 0 or a[2][0] + a[1][1] + a[0][2] == 0:
    print("Yes")
    exit()

print("No")