T= int(input())

def back(product,idx):
    global min
    if product > min:
        return
    if sum(visited) == n:
        if product < min:
            min = product
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            back(li[idx][i]+product,idx+1)
            visited[i]=0





for tc in range(1, T+1):
    n = int(input())
    li= [list(map(int,input().split())) for _ in range(n)]
    min =0
    for i in range(n):
        min += sum(li[i])
    visited=[0]*n
    back(0,0)
    print(f'#{tc} {min}')




