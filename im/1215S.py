for tc in range(1,11):

    n= int(input())
    li=[list(map(str,input())) for _ in range(8)]
    cnt=0

    # 가로

    for i in range(8):
        fel=[]
        for j in range(8):
            fel.append(li[i][j])
            if len(fel) ==n:
                if fel==fel[::-1]:
                    cnt+=1
                    fel.pop(0)
                else:
                    fel.pop(0)


    #세로

    for i in range(8):
        fel=[]
        for j in range(8):
            fel.append(li[j][i])
            if len(fel) == n:
                if fel == fel[::-1]:
                    cnt += 1
                    fel.pop(0)
                else:
                    fel.pop(0)




    print(f'#{tc} {cnt}')


