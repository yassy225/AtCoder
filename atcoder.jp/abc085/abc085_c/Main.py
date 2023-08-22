n,y = map(int, input().split())
a = b = c = -1

#X
for i in range(2001):
    #Y
    for j in range(2001):
        if 9000*i + 4000*j == y - 1000 * n:
            a = i
            b = j
            c = n - a - b
            if a >= 0 and b >= 0 and c >= 0:
                print("{} {} {}".format(a,b,c))
                exit()

print("-1 -1 -1")