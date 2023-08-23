for _ in range(1,11):
    tc= int(input())
    li=[]
    ans=[]

    for i in range(100):
        li.append(list(map(int, input().split())))


    for i in range(100):
        garo = 0
        sero = 0
        degak1 = 0
        degak2 = 0
        for j in range(100):
            garo += li[i][j]
            ans.append((garo))
            sero += li[j][i]
            ans.append(sero)

            if i==j:
                degak1 +=li[i][j]
                ans.append(degak1)

            if i+j ==99:
                degak2 +=li[i][j]
                ans.append(degak2)

    print(f'#{tc} {max(ans)}')






