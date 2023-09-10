def DFS(node):
    visited1[node]=1
    print(node, end=' ')

    for next in range(V+1):
        if G[node][next]==1 and visited1[next]==0:
            DFS(next)


def BFS(node):
    queue=[node]
    
    while queue:
        start= queue.pop(0)
        if visited2[start]==0:
            visited2[start]=1
            print(start, end=' ')

            for next in range(V+1):
                if G[start][next]==1 and visited2[next]==0:
                        queue.append(next)




V,E,S = map(int, input().split())
visited1=[0]*(V+1)
visited2=[0]*(V+1)

G=[[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    x, y= map(int, input().split())
    G[x][y]=1
    G[y][x]=1

DFS(S)
print()
BFS(S)    