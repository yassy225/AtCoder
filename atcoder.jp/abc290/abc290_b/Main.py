n,k = map(int, input().split())
s = list(input())

for i in range(n):
    if s[i] == 'x' or k <= 0:
        print('x', end="")
    else:
        print('o', end="")
        k -= 1
print()