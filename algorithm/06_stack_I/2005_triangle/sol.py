import sys
sys.stdin = open('input.txt')


memo = [[0 for _ in range(11)] for _ in range(11)]  # 2차원 초기화
for i in range(10):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
for i in memo:
    print(i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(memo[i][j], end=' ')
        print()

