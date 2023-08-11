import sys

sys.stdin = open('input.txt')


# 노드 번호를 받아서 해당 노드부터 조사를 시작
def DFS(node):
    visited[node] = True  # 방문 했다.

    print(node, end=' ')
    for next in range(1, V + 1):
        # 다음 조사 가능 여부
        if matrix[node][next] == 1 and visited[next] == 0:
            DFS(next)


# V = node의 개수
# E = Edge 간선의 개수
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))
visited = [False] * (V + 1)  # 노드가 7개인데, 7번 인덱스까지 필요하니까 7+1 개의 값을 가진 리스트
# 이동 가능 정보 2차원 리스트
matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 모든 간선 순회
# for i in range(E):
#     print(data[i * 2], data[i * 2 + 1])
for i in range(0, E * 2, 2):
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i + 1]] = 1
    matrix[data[i + 1]][data[i]] = 1
    '''
    matrix[1][2] = 1
    matrix[2][1] = 1

    matrix[data[0]][data[1]] = 1
    matrix[data[1]][data[0]] = 1

    matrix[data[2]][data[3]] = 1
    matrix[data[3]][data[2]] = 1
    '''

print(V, E)
print(data)
from pprint import pprint

pprint(matrix)
DFS(1)