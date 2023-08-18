from collections import deque

for tc in range(1,11):
    n = input()
    li =deque(list(map(int, input().split())))


    cnt = 1
    while True:
        if cnt >5:
            cnt =1
        a= li.popleft()-cnt

        if a <=0:
            li.append(0)
            break
        li.append(a)
        cnt+=1

    print(f'#{n}',*li, end=' ')
    print()




