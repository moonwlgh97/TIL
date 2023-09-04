from collections import deque
q=deque()
result = []
n= int(input())

for i in range(1,n+1):
    q.append(i)

while q:
        result.append(q.popleft())
        if q:
            q.append(q.popleft())


print(*result)