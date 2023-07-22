N = int(input())
a = list(map(int, input().split()))
alice=0
bob=0

while N > 0:
    alice += max(a)
    a[a.index(max(a))] = 0

    N -= 1
    if(N == 0):
        break

    bob += max(a)
    a[a.index(max(a))] = 0

    N -= 1

print(alice - bob)
