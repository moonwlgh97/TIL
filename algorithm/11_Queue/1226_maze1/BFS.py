import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                maze[nx][ny] = 1

                queue.append((nx, ny))
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                print(f'#{tc} {BFS(i, j)}')