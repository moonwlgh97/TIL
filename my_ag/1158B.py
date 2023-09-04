from collections import deque

q=deque()
result=[]

n ,k= map(int, input().split())

for i in range(1,n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')
