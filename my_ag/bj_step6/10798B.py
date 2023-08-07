import sys
input = sys.stdin.readline

a=[list(input()) for _ in range(5)]

for i in range(5):
    for j in range(5):

     print(a[j][i], end='')
