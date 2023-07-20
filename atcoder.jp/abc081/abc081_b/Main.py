n = int(input())
a = list(map(int, input().split()))
result=0
flg=True

while flg:
    for i in range(n):
        if a[i] % 2 != 0:
            flg = False
            break
    for j in range(n):
        a[j] //= 2
    if flg: result += 1
print(result)