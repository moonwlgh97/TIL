from collections import deque

T = int(input())

for tc in range(1,T+1):
    n ,m = map(int, input().split())

    q = deque(list(map(int, input().split())))


    for _ in range(m):
        a = q.popleft()
        q.append(a)

    print(f'#{tc} {q[0]}')


