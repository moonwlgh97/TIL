# 순열
#r : 내가 사용하고 있는 값의 수
def perm(r):
    #재귀함수
    #종료조건 (재귀의 기저까지 왔을떄의 상황)

    if r == n:
        #내가 원하는 무언가를 실행
        return
    else:
        # 내가 가진 arr의 모든 원솔ㄹ 매번 사용할 것인지 체크
        for i in range(n):
            # arr i 번째 요소를 쓴적이 있는지 없는지를 기준으로 판단
            if visitied[i] == True:
                continue

            perm(r+1) # 다음번 조사에는 한개 채웠다

# nPr : n개의 요소중 r개를 사용하여 순열
arr=[1,2,3]
n = len(arr)
# 내가 perm 함수 호출시 arr의 i번째 값을 썼었던 적이 있는지 판별
visitied = [0] *n
