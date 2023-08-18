
def bfs(S,G):
    visited=[0]*(V+1)
    q=[]
    q.append(S)
    visited[S] =1

    while q:
        start = q.pop(0)
        for next in range(V+1):
            if li[start][next] ==1 and visited[next]==0:
                q.append(next)
                visited[next] = visited[start]+1


    if visited[G]:
        return visited[G]-1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # 노드 간선
    li= []
    for _ in range(V+1):
        li.append([0]*(V+1))

    for _ in range(E):
        n ,m = map(int,input().split())
        li[n][m] = 1
        li[m][n] =1

    S,G = map(int,input().split())

    print(f'#{tc} {bfs(S,G)}')
