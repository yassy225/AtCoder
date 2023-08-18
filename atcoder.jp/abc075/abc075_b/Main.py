h,w = map(int, input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        cnt = 0

        #8方向をチェックする
        if s[i][j] == '.':
            #左上
            if i>0 and j>0 and s[i-1][j-1] == '#':
                cnt += 1
            #上
            if i>0 and s[i-1][j] == '#':
                cnt += 1
            #右上
            if i>0 and j<w-1 and s[i-1][j+1] == '#':
                cnt += 1
            #左
            if j>0 and s[i][j-1] == '#':
                cnt += 1
            #右
            if j<w-1 and s[i][j+1] == '#':
                cnt += 1
            #左下
            if i<h-1 and j>0 and s[i+1][j-1] == '#':
                cnt += 1
            #下
            if i<h-1 and s[i+1][j] == '#':
                cnt += 1
            #右下
            if i<h-1 and j<w-1 and s[i+1][j+1] == '#':
                cnt += 1
        else:
            print('#', end='')
            continue

        print(cnt, end="")
    print()