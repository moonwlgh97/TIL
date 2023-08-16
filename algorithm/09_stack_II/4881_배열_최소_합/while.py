import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N  # 최솟값 초기화
    visited = [0] * N   # 행의 방문 여부를 저장하는 리스트
    # 시작점
    now = 0
    # 누적값
    acc = 0
    # stack 에 담는 것은 다음 조사 대상
    # 매번 조사 대상마다 visited는 별개로 처리해서 검사해야하니
    # 새 리스트로 만들어서 복사
    stack = [(now, acc, visited[:])]
    while stack:
        # 다음 조사 대상
        now, acc, visited = stack.pop()
        if acc > result:
            continue
        # 언제까지 조사 할거냐? -> now 가 N이 되면 모든 열에 대한 탐색
        if now == N:
            if acc < result:
                result = acc
        else:
            # 현재 열(now)에서 가능한 모든 행(row)를 탐색
            for row in range(N):
                # 아직 방문한적 없다면,
                if visited[row] == 0:
                    # visited[row] = 1  # 현재 행 값 쓰겠다.
                    new_visited = visited[:]
                    new_visited[row] = 1
                    stack.append((now + 1, acc + arr[now][row], new_visited))
    print(f'#{tc} {result}')