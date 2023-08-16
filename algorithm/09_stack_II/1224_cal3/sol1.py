import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    _ = int(input())
    arr = list(input())
    result = []
    stack = []
    for token in arr:
        if token.isdecimal():   # 숫자이면
            result.append(token) # result에 append
        else:
            if not stack:   # 스택이 비어있으면  append
                stack.append(token)
            else:   # 스택이 있으면
                if token == '(':    # 토큰이 ( 이면
                    stack.append(token) # 그대로 append (최하위 우선순위 -> 제일 위에 append)
                elif token == ')':  # 토큰이 ) 이면
                    while stack[-1] != '(': # ( 가 나올 때까지
                        result.append(stack.pop())  # pop해서 result에 append
                    stack.pop() # ( 없앰

                elif token == '*' or token == '/':  # * 또는 / 이면
                    # 스택이 비어있지 않고 최상단 스택이 같은 우선순위 값이 나올때까지
                    while stack and (stack[-1] == '*' or stack[-1] == '/'):
                        result.append(stack.pop())  # pop해서 result에 append
                    stack.append(token) # 스택에 append
                elif token == '+' or token == '-':  # + 또는 - 이면
                    # 스택이 비어있지 않고 최상단 스택이 최상위 우선순위인 ( 나올때까지
                    while stack and stack[-1] != '(':
                        result.append(stack.pop())  # pop해서 result에 append
                    stack.append(token) # 스택에 append
    while stack:    # 남은 연산자 그대로 출력
        result += stack.pop()

    stack = []
    for token in result: # 계산
        if token.isdecimal():
            stack.append(token)
        else:
            if token == '+':
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n1+n2)
            elif token == '-':
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 - n1)
            elif token == '*':
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n1 * n2)
            elif token == '/':
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.append(n2 / n1)

    print(f'#{tc} {stack.pop()}')
