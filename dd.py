T = int(input())

def bfs():
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    

    while q:
        a,b = q.pop(0)

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if li[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]= visited[a][b]+1


                elif li[nx][ny]==3:
                    return visited[a][b]
    return 0





for tc in range(1,T+1):
    n = int(input())
    li=[]
    q=[]
    visited=[]
    for i in range(n):
        visited.append([0]*n)

    for _ in range(n):
        li.append(list(map(int, input())))

    for x in range(n):
        for y in range(n):
            if li[x][y]==2:
                q.append((x,y))

    print(f'#{tc} {bfs()}')            

