n = int(input())
old_n = n
sn = 0

while n > 0:
    sn += (n % 10)
    n //= 10

if old_n % sn == 0:
    print("Yes")
else:
    print("No")