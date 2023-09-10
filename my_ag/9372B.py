import sys
input=sys.stdin.readline
T= int(input())



def dfs(node):
    global cnt
    visited[node]=1

    for next in range(1,v+1):
        if G[node][next]==1 and visited[next]==0:
            cnt+=1
            dfs(next)
            




for _ in range(T):
    v, e= map(int,input().split())
    cnt=0
    G=[[0]*(v+1) for _ in range(v+1)]
    visited=[0]*(v+1)
    for _ in range(e):
        x,y =map(int,input().split())
        G[x][y]=1
        G[y][x]=1
    
    dfs(1)

    print(cnt)
    
