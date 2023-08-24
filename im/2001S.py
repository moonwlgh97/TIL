T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    li=[list(map(int,input().split())) for _ in range(n)]
    kill=[]


    for i in range(n-m+1):
        for j in range(n-m+1):

           sum=0

           for x in range(m):
               for y in range(m):
                   sum += li[i+x][j+y]
           kill.append(sum)


    print(f'#{tc} {max(kill)}')
