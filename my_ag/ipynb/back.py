m=int(input())
li=[]
stack=[]
for i in range(m):
    li.append(list(map(int,input())))
    stack.append([0]*m)
dx=[0,0,-1,1]
dy=[1,-1,0,0]
x,y=4,3
def back(x,y):
    if li[x][y]==3:
        print(x,y)
        return
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<m and stack[nx][ny] == 0 and li[nx][ny]==0:
            stack[nx][ny]=1
            back(nx,ny)
stack[x][y]=1
back(x,y) 
print(stack)               

           