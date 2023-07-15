# coding: utf-8
# Your code here!

h,w = map(int, input().split())

if h % 2 == 0:
    row = h // 2
else:
    row = h // 2 + 1

if w % 2 == 0:
    col = w // 2
else:
    col = w // 2 + 1

if h == 1:
    print(w)
elif w == 1:
    print(h)
else:
    print(row*col)
