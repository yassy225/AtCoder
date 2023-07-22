N = int(input())
S = str(input())

result=0

if S.find('A')+1 > result:
    result = S.find('A') + 1
if S.find('B')+1 > result:
    result = S.find('B') + 1
if S.find('C')+1 > result:
    result = S.find('C') + 1

print(result)