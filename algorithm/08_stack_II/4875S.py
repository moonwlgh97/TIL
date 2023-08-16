T= int(input())

def bfs():
    while stack:
        x,y=stack.pop(0)
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]

        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            if 0<= nx < n and 0<= ny <n and visited[nx][ny]==0:

                if li[nx][ny] == 0:
                    visited[nx][ny]=1
                    stack.append((nx,ny))


                elif li[nx][ny]==3:
                    return 1    
    return 0    





for tc in range(1,T+1):
    n = int(input())
    li =[]
    visited = []
    stack=[]
    for i in range(n):
        li.append(list(map(int, input())))
        visited.append([0]*n)

    for i in range(n):
        for j in range(n):
            if li[i][j] == 2:
                a,b = i,j

    visited[a][b]=1
    stack.append((a,b))

    print(f'#{tc} {bfs()}')

    