T = int(input())


for tc in range(1,T+1):
    n,m = map(int, input().split())
    li =[]
    ans=[]
    for i in range(n):
        li.append(list(map(int, input().split())))
    
   
    for x in range(n):
        for y in range(m):
            sum=li[x][y]

            for i in range(1,li[x][y]+1):
                 dx = [0,0,i,-i]
                 dy = [i,-i,0,0]

                 for z in range(4):
                    nx = x+dx[z]
                    ny = y+dy[z]

                    if 0<=nx<n and 0<= ny<m:
                        sum+=li[nx][ny]
                        ans.append(sum)


    print(f'#{tc} {max(ans)}')                

    