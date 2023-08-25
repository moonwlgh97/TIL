T = int(input())

for tc in range(1,T+1):
    print(f'#{tc}')
    n = int(input())
    li = [list(map(str, input().split())) for _ in range(n)]

    new_li=[['']*3 for _ in range(n)]

    #90
    for i in range(n):
        for j in range(n):
            new_li[i][0] += li[n-j-1][i]

    # 180

    for i in range(n):
        for j in range(n):
            new_li[i][1] +=li[n-i-1][n-j-1]


    # 270

    for i in range(n):
        for j in range(n):
            new_li[i][2] +=li[j][n-i-1]


    for i in range(n):
        print(*new_li[i])




