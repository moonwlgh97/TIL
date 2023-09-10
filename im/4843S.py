T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li= list(map(int, input().split()))
    ans=[]

    while len(li)>0:
        max_li = max(li)
        li.remove(max_li)
        ans.append(max_li)

        min_li = min(li)
        li.remove(min_li)
        ans.append(min_li)



    print(f'#{tc}', end= ' ')
    print(*ans, end=' ')
    print()
