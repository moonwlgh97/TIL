import sys
sys.stdin = open('input.txt')

def DFS(node):
    stack = [node]
    visited = [False] * (V+1)   # 노드가 7개인데, 7번 인덱스까지 필요하니까 7+1 개의 값을 가진 리스트
    while stack:    # stack에 (조사해야할 값)이 있는 동안
        start = stack.pop() # stack은 항상 LIFO 마지막에 들어간 요소 빼내서 쓸거다.
        if visited[start] == 0:
            visited[start] = True   # 방문 했다.
            print(start, end=' ')
            for next in range(V, 0, -1):
                if matrix[start][next] == 1 and visited[next] == 0:
                    stack.append(next)

V, E = map(int, input().split())
data = list(map(int, input().split()))
matrix = [[0]*(V+1) for _ in range(V+1)]

for i in range(0, E*2, 2):
    matrix[data[i]][data[i+1]] = 1
    matrix[data[i+1]][data[i]] = 1
DFS(1)