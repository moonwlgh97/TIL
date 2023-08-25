T = int(input())

for tc in range(1,T+1):
    n, k= map(int, input().split())

    li=[list(map(int, input().split())) for _ in range(n)]
    result=0

    for i in range(n):
        cnt=0
        for j in range(n):

            if li[i][j]==1:
                cnt+=1

            if li[i][j] == 0 or j== n-1:
                if cnt==k:
                    result+=1
                cnt=0

    for i in range(n):
        cnt1=0
        for j in range(n):
            if li[j][i] == 1:
                cnt1 +=1

            if li[j][i]==0 or j==n-1:
                if cnt1 ==k:
                    result+=1
                cnt1=0

    print(f'#{tc} {result}')


