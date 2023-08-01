import sys

# nは8進数、kは回数
n,k = map(int, input().split())

if n==0:
    print(0)
    sys.exit()

def eight2nine(num):
    nine = []
    while(num > 0):
        nine.insert(0,num%9)
        num //= 9

    return nine

for i in range(k):
    n = eight2nine(int(str(n),8))

    #8を5に変換
    for j in range(len(n)):
        if(n[j] == 8):
            n[j] = 5
    
    #リストを数値に変換
    n = "".join(map(str, n))

for k in range(len(n)):
    print(n[k], end='')
