n = int(input())
s = input()

for i in s:
    ch = ord(i) + n
    if ch > 90:
        ch = (ch - 90) + 64

    print(chr(ch),end="")
print()