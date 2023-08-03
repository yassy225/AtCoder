n = int(input())
a = list(map(int, input().split()))
num = []

for i in range(1, n+1):
    num.append(i)

sorted_a = sorted(a)

if (sorted_a == num):
    print("Yes")
else:
    print("No")