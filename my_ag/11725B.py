
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):


    for next in G[node]:
        if visited[next]==0:
            visited[next] = node
            dfs(next)


v = int(input())
e= v-1

G=[[] for _ in range(v+1)]
visited = [0]*(v+1)

for _ in range(e):
    i,j = map(int, input().split())
    G[i].append(j)
    G[j].append(i)


dfs(1)

for i in range(2,v+1):
    print(visited[i])



