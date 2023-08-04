X = int(input())
N = int(input())

cnt = 0
for i in range(N):
    a ,b = map(int, input().split())
    cnt = cnt +(a*b)

if cnt == X:
    print('Yes')
else:
     print('No')     
     

