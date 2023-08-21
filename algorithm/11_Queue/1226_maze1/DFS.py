import sys
sys.stdin = open('input.txt')


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                maze[nx][ny] = 1

                stack.append((nx, ny))
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                print(f'#{tc} {DFS(i, j)}')