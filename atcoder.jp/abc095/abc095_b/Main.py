n,x = map(int, input().split())

m = []
for _ in range(n):
    m.append(int(input()))

remain = x - sum(m)
count = n

while True:
    remain -= min(m)
    if remain < 0:
        break
    count += 1

print(count)