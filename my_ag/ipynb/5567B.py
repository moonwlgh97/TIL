import sys
input = sys.stdin.readline



def bfs(node):
    q=[node]
    while q:
        start= q.pop(0)
        for next in G[start]:
            if visited[next]==0:
                visited[next]=visited[start]+1
                q.append(next)

    visited[1]=0
    cnt =0

    for i in visited:
        if i==1 or i==2:
            cnt+=1

    if cnt==0:
        print(0)

    else:
        print(cnt)




n = int(input())
m= int(input())
G=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    i, j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)

bfs(1)
