a,b = map(int, input().split())

result_a = str(a) * b
result_b = str(b) * a

if a>b:
    print(result_b)
else:
    print(result_a)
