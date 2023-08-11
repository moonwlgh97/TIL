import sys
sys.stdin = open('input.txt')


def DFS(start):
    visited[start] = 1
    if start == 99:
        return
    for w in range(1, 100):
        if G[start][w] == 1 and visited[w] == 0:
            DFS(w)

for _ in range(10):
    tc, E = map(int, input().split())
    data = list(map(int, input().split()))

    G = [[0]*100 for _ in range(100)]
    visited = [0] * 100

    for i in range(E):
        G[data[i*2]][data[i*2+1]] = 1
    DFS(0)
    print(f'#{tc} {visited[99]}')
