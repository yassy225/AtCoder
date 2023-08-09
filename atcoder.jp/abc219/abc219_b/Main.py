s = [str(input()) for _ in range(3)]
t = list(input())

for i in range(len(t)):
    print(s[int(t[i])-1], end="")

print()