h,w,x,y = map(int, input().split())
s = [input() for _ in range(h)]
ans = 1
point_x = x-1
point_y = y-1

#左
for i in reversed(range(point_y)):
    if s[point_x][i] == '#':
        break
    else:
        ans += 1

#右
for i in range(point_y+1, w):
    if s[point_x][i] == '#':
        break
    else:
        ans += 1

#上
for i in reversed(range(point_x)):
    if s[i][point_y] == '#':
        break
    else:
        ans += 1

#下
for i in range(point_x+1, h):
    if s[i][point_y] == '#':
        break
    else:
        ans += 1
print(ans)