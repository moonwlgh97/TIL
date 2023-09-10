T = int(input())


for tc in range(1,T+1):

    n,k = map(int,input().split())
    stu=[i for i in range(1, n+1)]
    homework= list(map(int, input().split()))


    for i in range(k):
        stu.remove(homework[i])

    print(f'#{tc}',end= ' ')
    print(*stu, end=' ')
    print()
