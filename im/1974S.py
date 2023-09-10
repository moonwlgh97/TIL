T = int(input())

for tc in range(1,11):
    li=[list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        garo_check=[0]*10
        sero_check=[0]*10
        for j in range(9):
            garo_check[li[i][j]] +=1
            sero_check[li[j][i]] +=1
            if garo_check[li[i][j]] == 2 or sero_check[li[j][i]] ==2:
                result =0



    for i in range(0,9,3):
        for j in range(0,9,3):
            sam_check=[0]*10

            for x in range(3):
                for y in range(3):

                    sam_check[li[i+x][j+y]] +=1

                    if sam_check[li[i+x][j+y]] ==2:
                        result =0


    print(f'#{tc} {result}')