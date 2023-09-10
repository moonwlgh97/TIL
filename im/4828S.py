T=int(input())

for tc in range(1,T+1):
    n = int(input())
    li= list(map(int, input().split()))

    min=1000001
    max=0


    for i in range(n):
        if max < li[i]:
            max=li[i]

        if min > li[i]:
           min =li[i]


    print(f'#{tc} {max-min}')