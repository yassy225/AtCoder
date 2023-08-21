h,w = map(int, input().split())
s = [input() for _ in range(h)]
del_h = [] * h
del_w = [] * w

#行をチェック
for i in range(h):
    cnt = 0
    for j in range(w):
        if s[i][j] == '.':
            cnt += 1
    if cnt == w:
        del_h.append(i)

#列をチェック
for i in range(w):
    cnt = 0
    for j in range(h):
        if s[j][i] == '.':
            cnt += 1
        if cnt == h:
            del_w.append(i)

#圧縮処理
for i in range(h):
    if i in del_h:
        continue
    for j in range(w):
        if j in del_w:
            continue
        print(s[i][j], end="")
    print()