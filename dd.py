def bfs(node):
    q=[(node, 1)]
    visited[node]=0
    while q:
        start, cnt = q.pop(0)
        G[start].sort()

        for next in G[start]:
            if visited[next]==-1:
                
                visited[next]= (visited[start]+1)
                q.append(next)

n,m,r = map(int,input().split())
G= [[] for _ in range(n+1)]
visited = [-1] *(n+1)
q=[]

for _ in range(m):
    i, j = map(int, input().split())
    G[i].append(j)
    G[j].append(i)


bfs(r)
print(visited)