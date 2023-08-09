T = int(input())

for tc in range(1,T+1):
    text = input()
    stack = []
    for i in text:
        if i == '(' or i == '{':
            stack.append(i)
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()

        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == '}' or i == ')':
            stack.append(i)

    if len(stack) == 0:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')