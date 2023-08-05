import sys
n = int(input())
p = list(map(int, input().split()))

if(len(p) == 1):
    print("0")
    sys.exit()

lst = p[1::]
p_max = max(p)
lst_max = max(lst)

if p[0] == lst_max:
    print("1")
elif p[0] == p_max:
    print("0")
else:
    print(p_max - p[0] + 1)