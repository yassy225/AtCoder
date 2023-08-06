n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))

ave = []

#平均気温からの差を求める
for i in range(len(h)):
    ave.append(abs(a - (t - h[i] * 0.006)))

#平均気温に一番近い地点を求める
print(ave.index(min(ave))+1)