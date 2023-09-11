T= int(input())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    stack=[(x,y)]
    G[x][y]=0
    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < m and 0<= ny < n and G[nx][ny]==1:
                stack.append((nx,ny))
                G[nx][ny]=0





for _ in range(T):
    m,n,k = map(int,input().split())
    G=[[0]*(n) for _ in range(m)]
    cnt=0
    stack=[]

    for _ in range(k):
        x, y = map(int, input().split())

        G[x][y]=1


    for i in range(m):
        for j in range(n):
            if G[i][j]==1:
                dfs(i,j)
                cnt+=1


    print(cnt)