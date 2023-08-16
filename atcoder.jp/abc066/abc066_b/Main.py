#s = list(input())
s = input()
A = []
s2 = str(s)
tmp = 0

for i in range(1,len(s)):
    s2 = s2[0:len(s)-i]
    #print("s :",s)
    #print("s2:",s2)

    #偶文字かどうかを判定
    for j in range(1,len(s2)):
        l = s2[:j]
        if s2 == l * 2:
            A.append(len(l * 2))

print(max(A))