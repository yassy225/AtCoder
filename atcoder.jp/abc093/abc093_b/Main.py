a,b,k = map(int, input().split())

#aとbの差が2k未満
if (b-a) < 2*k:
    for i in range(a, b+1):
        if i<=a+k-1 or i>=b-k+1:
            print(i)

#aとbの差が2k以上
if (b-a) >= 2*k:
    for i in range(a, a+k):
        print(i)

    for j in range(b-k+1, b+1):
        print(j)