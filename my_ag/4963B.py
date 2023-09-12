
dx=[1,-1,0,0, 1, 1, -1, -1]
dy=[0,0,1,-1, 1, -1, 1, -1]


def dfs(x,y):
    stack=[(x,y)]
    li[x][y]=0

    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx= x+ dx[i]
            ny= y+ dy[i]

            if 0<=nx<h and 0<=ny<w and li[nx][ny]==1:
                stack.append((nx,ny))
                li[nx][ny]=0




while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    li=[list(map(int, input().split())) for _ in range(h)]
    cnt=0
    stack=[]

    for i in range(h):
        for j in range(w):
            if li[i][j]==1:
                dfs(i,j)
                cnt+=1

    print(cnt)            