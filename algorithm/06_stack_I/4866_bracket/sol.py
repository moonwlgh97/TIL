import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    word = input()

    # 최종 결괏값
    result = 1
    stack = []
    op = '({'
    for char in word:
        # if char == '(' or char == '{':
        if char in op:
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack: # 스택이 비었는데
                    result = 0
                    # 더 이상 조사 할 필요 없다.
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
        # print(stack, char)

    if stack:
        result = 0

    print(f'#{tc} {result}')