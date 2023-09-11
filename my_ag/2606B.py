def dfs(node):
    visited[node]=1

    for next in range(V+1):
        if G[node][next]==1 and visited[next]==0:
            dfs(next)




V= int(input())
E= int(input())
visited=[0]*(V+1)
G=[[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    x,y = map(int,input().split())
    G[x][y]=1
    G[y][x]=1

dfs(1)
print(sum(visited)-1)