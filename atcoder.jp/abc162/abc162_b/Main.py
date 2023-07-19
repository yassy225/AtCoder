def fizzbuzz(number):
    if(number % 3 != 0 and number % 5 != 0):
        return number
    else:
        return 0

sum = 0
n = int(input())

for i in range(n+1):
    sum += fizzbuzz(i)

print(sum)