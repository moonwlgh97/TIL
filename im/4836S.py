T= int(input())

for tc in range(1,T+1):
    li=[[0]*10 for _ in range(10)]
    n= int(input())
    cnt=0

    for _ in range(n):
        r1,c1,r2,c2,color=map(int, input().split())

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                li[i][j] += color


    for i in range(10):
        for j in range(10):
            if li[i][j]==3:
                cnt +=1

    print(f'#{tc} {cnt}')


