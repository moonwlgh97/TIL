import heapq
import sys
input = sys.stdin.readline

def bfs(start):
    global total
    q=[*G[start]]
    visited[start]=1
    heapq.heapify(q)

    while q:
        w,s = heapq.heappop(q)

        if visited[s]==0:
            visited[s]=1
            total +=w

            for w, next in G[s]:
                if visited[next]==0:
                    heapq.heappush(q,(w,next))



v,e = map(int,input().split())
G=[[] for _ in range(v+1)]
visited=[0]*(v+1)
total =0

for _ in range(e):
    n1,n2,w = map(int,input().split())
    G[n1].append((w,n2))
    G[n2].append((w,n1))

bfs(1)
print(total)