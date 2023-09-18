def bfs():
    dx=[1,-1,0,0,1,1,-1,-1]
    dy=[0,0,1,-1,1,-1,1,-1]

    while q:
        x,y = q.pop(0)
        for i in range(8):
            nx= x+dx[i]
            ny= y+dy[i]

            if 0<=nx<n and 0<=ny< m and li[nx][ny]==0:
                li[nx][ny] = li[x][y]+1
                q.append((nx,ny))





n, m = map(int, input().split())
li=[list(map(int, input().split())) for _ in range(n)]
q=[]

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            q.append((i,j))

bfs()
max=0

for i in range(n):
   for j in range(m):
       if max < li[i][j]:
           max = li[i][j]

print(max-1)

