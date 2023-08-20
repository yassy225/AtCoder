n = int(input())
s = []
for i in range(n):
    a,b=input().split()
    s.append([a, int(b)])
sum = 0

#合計
for i in range(n):
    sum += s[i][1]

majority = sum // 2 + 1

#過半数を求める
for i in range(n):
    if s[i][1] >= majority:
        print(s[i][0])
        exit()

print("atcoder")