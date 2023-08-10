n = int(input())
s = [input() for _ in range(n)]

ac = wa = tle = re = 0

for i in s:
    if i == "AC":
        ac += 1
    elif i == "WA":
        wa += 1
    elif i == "TLE":
        tle += 1
    else:
        re += 1

print("AC x",ac)
print("WA x",wa)
print("TLE x",tle)
print("RE x",re)