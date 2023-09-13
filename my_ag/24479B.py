import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(node):
    global cnt

    visited[node]=cnt
    G[node].sort()

    for next in G[node]:
        if visited[next]==0:
            cnt+=1
            dfs(next)




n,m,r = map(int,input().split())
G=[[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt=1

for _ in range(m):
    i, j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)
dfs(r)

for i in range(1,n+1):
    print(visited[i])