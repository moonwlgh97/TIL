import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(x, y, cnt):
    q = [(x, y, cnt)]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return cnt
                visited[nx][ny] = cnt + 1
                q.append((nx, ny, cnt+1))
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(f'#{tc} {BFS(i, j, 0)}')