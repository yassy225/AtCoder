h,w = map(int, input().split())
a = [list(input().split()) for _ in range(h)]

for i in range(w+2):
    print('#', end='')

print('')

for j in range(h):
    a[j].insert(0, '#')
    a[j].insert(len(a[0]), '#')
    print(''.join(a[j]))


for j in range(w+2):
    print('#', end='')
print('')