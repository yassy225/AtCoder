n,a,b = map(int, input().split())
sum = 0

for i in range(n+1):
    w = x = y = z = 0
    
    if(i == 10000 and a == 1):
        sum += i
        continue
    
    elif(i <= 9999 and i >= 1000):
        w = i // 1000
        x = i % 1000 // 100
        y = i % 100 // 10
        z = i % 10
        if((w+x+y+z) >= a and (w+x+y+z) <= b):
            sum += i
        
    elif(i <= 999 and i >= 100):
        x = i // 100
        y = i % 100 // 10
        z = i % 10
        if((x+y+z) >= a and (x+y+z) <= b):
            sum += i

    elif(i <= 99 and i >= 10):
        y = i // 10
        z = i % 10
        if((y+z) >= a and (y+z) <= b):
            sum += i
    
    else:
        if(i >= a and i <= b):
            sum += i

print(sum)