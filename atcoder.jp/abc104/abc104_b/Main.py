S = str(input())
result = "AC"

#条件1
if S[0] != 'A':
    result = "WA"

#条件2
tmp = S[2:]
tmp = tmp[:-1]

flg = False
for i in range(len(tmp)):
    if tmp[i] == 'C':
        if not flg: flg = True
        else: result = "WA"

if not flg: result = "WA"

#条件3
tmp = S.replace('C', 'c', 1)

if not tmp[1:].islower():
    result = "WA"

print(result)