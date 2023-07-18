import sys

k=int(input())
a,b=map(int, input().split())

for num in range(a, b+1):
    if(num % k == 0):
        print("OK")
        sys.exit()
print("NG")