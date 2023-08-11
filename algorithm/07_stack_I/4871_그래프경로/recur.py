import sys
sys.stdin = open('input.txt')


def DFS(start):
    # 조사 지점 방문 표시
    visited[start] = 1
    # 현재 조사 지점이 도착지점인 G라면
    if start == G:
        # 조사 종료
        return  # 현재 조사 시점을 방문 표시하였으므로 반환값 없이 종료하여도 된다.
    # 1번 노드부터 끝번 노드까지 전수조사
    for next in range(1, V+1):
        # start 지점에서 next지점에 갈 수 있고, next 지점을 방문한적 없다면
        if data[start][next] and not visited[next]:
            DFS(next)   # 다음 위치 조사 시작

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0]*(V+1) for _ in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)
    # 간선 정보 입력 받기
    for i in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1
    # 시작지점 S, 도착지점 G
    S, G = map(int, input().split())
    DFS(S)
    print(f'#{tc} {visited[G]}')