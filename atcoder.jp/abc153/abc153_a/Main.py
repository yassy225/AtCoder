monster,serval = map(int, input().split())

counter = int(monster / serval)

if monster % serval > 0:
    counter = counter + 1

print(counter)
