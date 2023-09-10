for tc in range(1,11):
    n= int(input())
    li=[list(map(int, input().split())) for _ in range(n)]

    cnt =0
    for j in range(n):
        r, c = 0, j
        stack = []

        while r<n:
            if not stack and li[r][c]==1:
                stack.append(1)

            elif stack and li[r][c]==2:
                cnt+= 1
                stack.pop()
            r+=1

    print(f'#{tc} {cnt}')

