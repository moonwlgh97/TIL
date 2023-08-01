import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    sample = list(map(int, input().split()))
    temp = 0 # 구간합 임시로 저장
    sum_list = []

    for i in range(N-M+1):
        temp = 0

        for j in range(i,i+M):
            temp = temp + sample[j]
        sum_list.append(temp)


    result = max(sum_list) - min(sum_list)
    print(f'#{tc} {result}')