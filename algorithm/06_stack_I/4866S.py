T= int(input())

for tc in range(1, T+1):
    stack = []
    s = input()
    for i in s:
        if i =='{' or i =='(':
            stack.append(i)
        elif i == '}':
            if len(stack) != 0 and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(i)
                break

        elif i == ')':
            if len(stack) != 0 and stack[-1]=='(':
                stack.pop()

            else:
                stack.append(i)
                break

    if len(stack) ==0:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')