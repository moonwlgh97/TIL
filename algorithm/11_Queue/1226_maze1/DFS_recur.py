import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] != 1 and not visited[nx][ny]:
            if maze[nx][ny] == 3:
                visited[nx][ny] = 1
                return 1
            maze[nx][ny] = 1
            result = DFS(nx, ny)
            if result:
                return result
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                DFS(i, j)
                break
            if maze[i][j] == 3:
                x, y = i, j
    print(f'#{tc} {visited[x][y]}')