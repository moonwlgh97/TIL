import heapq
import sys
input = sys.stdin.readline

q=[]

n= int(input())

for _ in range(n):
    li = list(map(int,input().split()))

    for num in li:
        if len(q) <n:
            heapq.heappush(q,num)

        else:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q,num)

print(q[0])

