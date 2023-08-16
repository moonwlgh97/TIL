t = int(input())

def search(now, acc):
    global  result
    # 가지치기, 내 누적값이 최종 결과 값보다 한번이라도 커지면 조사 x
    if acc > result:
        return
    #언제까지 조사? now  -> N
    if now == n:
        if acc < result:
            result = acc
    else:
        for row in range(n):
            # 아직 방문한적 없다면
            if visited[row] ==0:
                visited[row] =1 # 현재 행 값 쓰겠다              search(now+1, acc+ arr[now][row])
                visited[row] = 0



for tc in range (1, t+1):
    n = int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    result = 10*n 
    visited = [0] *n # 행의 방문 여부를 저장하는 리스트
    # 시작점 누적값
    search(0,0)
    print(f'{tc} {result}')