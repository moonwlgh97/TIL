import pprint

def DFS(start, end):
    visited[start] =1

    for next in range(v+1):
        if G[start][next] ==1 and visited[next]==0:
            DFS(next,end)

    if visited[end]:
        return 1
    else:
        return 0



T= int(input())

for tc in range(1,T+1):
    v, e = map(int,input().split()) # v는 노드 e 는 간선
    G=[[0 for _ in range(v+1)] for _ in range(v+1)]
    visited=[0]*(v+1)
    for _ in range(e):
        n_start, n_end = map(int,input().split())
        G[n_start][n_end] =1
    
    
    r_s, r_e = map(int, input().split())
    
    print(f'#{tc} {DFS(r_s,r_e)}')    

      
