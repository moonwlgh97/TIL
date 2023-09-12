import sys
input = sys.stdin.readline

def bfs(x,k):
    q=[x]

    while q:
        start=q.pop(0)

        for next in G[start]:
            if visited[next]==0:
                visited[next]=visited[start]+1
                q.append(next)

    visited[1]=0            
    
    if k in visited:
        for i in range(len(visited)):
            if visited[i]==k:
                print(i)
    else:
        print(-1)
               
            



n,m,k,x = map(int, input().split())
G=[[] for _ in range(n+1)]
visited = [0]*(n+1)


for _ in range(m):
    i, j = map(int,input().split())
    G[i].append(j)

bfs(x,k)
