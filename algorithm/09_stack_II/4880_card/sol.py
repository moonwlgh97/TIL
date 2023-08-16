import sys
sys.stdin = open('input.txt')


def match(start, end):
    if start == end:
        return start
    center = (start+end) // 2
    left = match(start, center)
    right = match(center+1, end)

    winner = (player[left] - player[right]) % 3
    if winner == 2:
        return right
    else:
        return left

    # if player[left] == player[right]:
    #     return left
    # # 1 : 가위, 2 : 바위, 3 : 보
    # if player[left] == 1 and player[right] == 2:
    #     return right
    # if player[left] == 1 and player[right] == 3:
    #     return left
    # if player[left] == 2 and player[right] == 1:
    #     return left
    # if player[left] == 2 and player[right] == 3:
    #     return right
    # if player[left] == 3 and player[right] == 1:
    #     return right
    # if player[left] == 3 and player[right] == 2:
    #     return left

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    player = list(map(int, input().split()))
    print(match(0, N-1)+1)