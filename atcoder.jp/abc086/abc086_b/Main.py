a,b = input().split()
num = (int)(a+b)
flg = False

for i in range(10001):
    if i*i == num:
        flg = True

if flg:
    print("Yes")
else:
    print("No")