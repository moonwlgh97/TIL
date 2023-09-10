

def dfs(node):
    global cnt
    stack=[node]

    while stack:
        start=stack.pop()

        if visited[start]==0:
            visited[start]=cnt

            for next in range(V+1):
                if G[start][next]==1 and visited[next]==0:
                    stack.append(next)



V, E = map(int, input().split())
visited=[0]*(V+1)
G=[[0]*(V+1) for _ in range(V+1)]
cnt=0

for _ in range(E):
    x,y=map(int,input().split())
    
    G[x][y]=1
    G[y][x]=1

for i in range(1,V+1):
    if visited[i]==0:
        cnt+=1
        dfs(i)
    else:
        continue  

print(cnt)     

   
    


 



