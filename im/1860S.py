T= int(input())

for tc in range(1,T+1):
    N, M, K = map(int, input().split()) #N- 사람수 , # M-붕어빵 시간, K-붕어빵 수
    sonnim = list(map(int, input().split()))
    sonnim.sort()
    result='Possible'
    for i in range(N):

        boong = (sonnim[i]//M)*K - (i+1)

        if boong < 0 :
            result = 'Impossible'
            break

    print(f'#{tc} {result}')






