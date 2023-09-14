import sys
sys.setrecursionlimit(100000)
input= sys.stdin.readline

def dfs(node):
    global cnt
    visited[node]=cnt
    G[node].sort(reverse=True)


    for next in G[node]:
        if visited[next]==0:
            cnt+=1
            dfs(next)


n,m,r = map(int, input().split())
G=[[] for _ in range(n+1)]
visited=[0]*(n+1)
cnt=1

for _ in range(m):
    i, j = map(int, input().split())

    G[i].append(j)
    G[j].append(i)

dfs(r)

for i in range(1,n+1):
    print(visited[i])


