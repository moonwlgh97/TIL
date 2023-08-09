T = int(input())

for tc in range(1,T+1):
    text = input()
    stack = []

    for i in text:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i== stack[-1]:
                stack.pop()
            else:
                stack.append(i)


    print(f'#{tc} {len(stack)}')