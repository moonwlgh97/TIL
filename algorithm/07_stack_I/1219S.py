def DFS(start,end):
    visited[start] =1

    for next in range(100):
        if G[start][next] ==1 and visited[next]==0:
            DFS(next,end)


        if visited[end]:
            return 1
        else:
            return 0    




for _ in range(10):
    t, e = map(int, input().split())
    data = list(map(int, input().split()))
    G =[]
    visited = [0] *100
   

    for _ in range(100):
        G.append([0]*100)

    for i in range(e):
        G[data[i*2]][data[i*2+1]]=1


    print(f'#{t} {DFS(0,99)}')        

       

