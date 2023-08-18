T = int(input())

def bfs():
    while q:
        x,y = q.pop(0)
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx <n and 0<=ny<n and visited[nx][ny] ==0:

                if li[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] =visited[x][y]+1



                elif li[nx][ny] ==3:

                    return visited[x][y]
    return 0



for tc in range(1,T+1):
    n = int(input())

    li = []
    visited = []
    q = []

    for i in range(n):
        li.append(list(map(int, input())))
        visited.append([0]*n)

    for i in range(n):
        for j in range(n):
            if li[i][j] ==2:
                a,b =i, j
                q.append((a,b))

    print(f'#{tc} {bfs()}')








