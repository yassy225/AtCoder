h = [str(input()) for _ in range(4)]
cnt = 0

for i in range(len(h)):
    if h[i] == "H":
        cnt += 1
        continue
    if h[i] == "2B":
        cnt += 2
        continue
    if h[i] == "3B":
        cnt += 3
        continue
    if h[i] == "HR":
        cnt += 4
        continue

if cnt == 10:
    print("Yes")
else:
    print("No")