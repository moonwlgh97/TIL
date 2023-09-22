import heapq
import sys
input = sys.stdin.readline

n ,m = map(int,input().split())
li= list(map(int,input().split()))
heapq.heapify(li)
for _ in range(m):
    x=heapq.heappop(li)
    y=heapq.heappop(li)

    heapq.heappush(li,x+y)
    heapq.heappush(li, x + y)

print(sum(li))
