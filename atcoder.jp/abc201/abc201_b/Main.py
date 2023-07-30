n = int(input())
list = []
for i in range(n):
    s,t=input().split()
    list.append([s, int(t)])

newlist = sorted(list,key=lambda x: x[1], reverse=True)

print(newlist[1][0])