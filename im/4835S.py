T= int(input())

for tc in range(1, T+1):
    n ,m = map(int, input().split())
    li = list(map(int, input().split()))
    result=[]
    num = []
    for i in range(n):

       num.append(li[i])

       if len(num)==m:
           result.append(sum(num))
           num.pop(0)

    print(f'#{tc} {max(result)-min(result)}')
