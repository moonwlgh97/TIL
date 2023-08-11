import sys
sys.stdin = open('input.txt')


# N이 0, 10, 20 일때, 각각 0, 1, 3의 경우의 수
# N이 20일때는 N이 0일때 경우의 수의 2배와, 10일때의 경우의 수를 더한 만큼이 된다.
# 즉, N이 30일때는 (1 * 2) + 3 = 5
# N이 40일 때는, (3 * 2) + 5 = 11
memo = [0, 1, 3]
for i in range(2, 30):
    memo.append(memo[i] + memo[i-1]*2)
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {memo[N//10]}')