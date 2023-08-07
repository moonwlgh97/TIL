
a=[]
for i in range(100):
    a.append([0]*100)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            a[i][j] = 1
cnt=0
for i in range(100):
    cnt = cnt + sum(a[i])
print(cnt)    

