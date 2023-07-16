n = int(input())
a = int(input())

remain = n % 500

if(remain <= a):
    print("Yes")
else:
    print("No")