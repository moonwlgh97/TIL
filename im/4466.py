T= int(input())


for tc in range(1,T+1):
    n , k = map(int, input().split())
    scores=list(map(int, input().split()))
    ans=[]

    for _ in range(k):
            ans.append(max(scores))
            scores.remove(max(scores))

    print(f'#{tc} {sum(ans)}')

