import sys
input = sys.stdin.readline

def bfs(p1,p2):
    q = [p1]
    
    
    while q:
        start = q.pop(0)

        for next in G[start]:
            if visited[next]==0:
                visited[next]=visited[start]+1
                q.append(next)

    if visited[p2]:
        print(visited[p2])
         
    else:
        print(-1)
                      
                




n = int(input())
p1, p2 = map(int,input().split())
m= int(input())

G=[[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    i, j = map(int, input().split())

    G[i].append(j)
    G[j].append(i)


bfs(p1,p2)


