

def BFS(node):
    queue = [node]
    visited = [0] * (V + 1) 
    while queue:
        start = queue.pop(0)  
        if visited[start] == 0:
            visited[start] = 1  
            print(start, end=' ')
            for next in range(V+1):
               
                if matrix[start][next] == 1 and visited[next] == 0:
                    queue.append(next)

V, E = map(int, input().split())
data = list(map(int, input().split()))

matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(0, E * 2, 2):
    matrix[data[i]][data[i + 1]] = 1
    matrix[data[i + 1]][data[i]] = 1
BFS(1)