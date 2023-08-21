def bfs():

    while q:
        x, y = q.pop(0)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx <16 and 0<= ny <16 and visited[nx][ny]==0:

                if li[nx][ny]== 0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                elif li[nx][ny] == 3:
                    return 1
    return 0




for tc in range(1,11):
    t= int(input())
    li=[]
    visited = []
    q =[]
    for i in range(16):
        li.append(list(map(int, input())))
        visited.append([0]*16)

    for i in range(16):
        for j in range(16):
            if li[i][j] ==2:
                a,b =i,j
                q.append((a,b))

    print(f'#{t} {bfs()}')