T = int(input())

for tc in range(1,T+1):
    n = int(input())
    li = list(map(int, input().split()))
    max_num=0
    for i in range(n-1):
        for j in range(i+1,n):
            num=li[i]*li[j]
            str_num=str(num)

            for k in range(len(str_num)-1):
                if str_num[k] > str_num[k+1]:
                    break

            else:
                if max_num < num:
                    max_num = num

    if max_num==0:
        print(f'#{tc}',-1)
    else:
        print(f'#{tc} {max_num}')









