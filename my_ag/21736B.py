def bfs():
    global cnt

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<= ny < m and li[nx][ny]!='X' and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1

                if li[nx][ny]=='P':
                    cnt+=1


n,m = map(int, input().split())
li= [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt=0
q=[]

for i in range(n):
    for j in range(m):
        if li[i][j]=='I':
            q.append((i,j))
            visited[i][j]=1

bfs()

if cnt == 0:
    print('TT')
else:
    print(cnt)

