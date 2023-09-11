dx=[1,-1,0,0, 1, 1, -1, -1]
dy=[0,0,1,-1, 1, -1, 1, -1]





w, h = map(int, input().split())
li=[list(map(int, input().split())) for _ in range(h)]
cnt=0
stack=[]

for i in range(h):
    for j in range(w):
        if li[i][j]==1:
            bfs(i,j)
            cnt+=1