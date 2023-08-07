import sys
input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(9)]
a_max = 0
X = 0
Y = 0

for i in range(9):
    for j in range(9):

        if a[i][j] >= a_max:
            a_max = a[i][j]
            X = i+1
            Y= j+1

print(a_max)  
print(X, Y)          
