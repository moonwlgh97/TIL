T = int(input())


for tc in range(1,T+1):
    n ,m = map(int, input().split())

    li=[]
    ans=[]

    for _ in range(n):
        li.append(list(map(int, input().split())))

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for x in range(n):
        for y in range(m):
            sum=li[x][y]

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<m:
                    sum+=li[nx][ny]
                    ans.append(sum)


    print(f'#{tc} {max(ans)}')
                    
        
