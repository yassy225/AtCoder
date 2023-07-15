a,b = map(int, input().split())

add = a+b
sub = a-b
multi = a*b

if add > sub:
    ans = add
else: ans = sub

if ans < multi:
    ans = multi

print(ans)