import sys
sys.stdin= open('input.txt')
for _ in range(10) :
    T = int(input())

    array = []
    for i in range(100) :
        array.append(list(map(int, input().split())))

    # 가로줄의 합
    max_1 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[i][j]
        if sum > max_1 :
            max_1 = sum

    # 세로줄의 합
    max_2 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[j][i]
        if sum > max_2 :
            max_2 = sum

    # 대각선의 합
    max_3 = 0
    for i in range(100) :
        sum1 = 0 ; sum2 = 0
        sum1 += array[i][i]
        sum2 += array[i][99-i]
    if max(sum1, sum2) > max_3 :
        max_3 = max(sum1, sum2)

    print(f'#{T} {max(max_1, max_2, max_3)}')