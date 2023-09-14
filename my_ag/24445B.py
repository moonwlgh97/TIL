def bfs(node):
    global cnt
    q=[node]
    visited[node]=cnt


    while q:
        start=q.pop(0)

        G[start].sort(reverse=True)

        for next in G[start]:
            if visited[next]==0:
                q.append(next)
                cnt+=1
                visited[next]=cnt





n,m,r = map(int,input().split())
G=[[]for _ in range(n+1)]
visited=[0]*(n+1)
cnt=1

for _ in range(m):
    i,j = map(int, input().split())
    G[i].append(j)
    G[j].append(i)

bfs(r)

for i in range(1,n+1):
    print(visited[i])


