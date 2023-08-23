t=int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [list(map(int, input())) for _ in range(n)]
    mid = n//2
    sum=0
    middle_sum =0

    for i in range(mid+1):
        for j in range(mid-i, mid+i+1):
            sum += li[i][j] + li[n-i-1][j]

            if i==mid:
                middle_sum+=li[i][j]

    print(f'#{tc} {sum-middle_sum}')
