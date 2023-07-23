import sys

a,b = map(int, input().split())

board = ["1","2","3"],["4","5","6"],["7","8","9"]

for i in range(3):
    for j in range(3):
        if board[i].count(str(b)):
            if board[i].count(str(a)):
                print("Yes")
                sys.exit()

print("No")
            

