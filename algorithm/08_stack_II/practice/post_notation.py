cal = '2+3*4/5'
# 최종 결값값
result = ''
# 연산자 모아둘 stack
stack = []

# 전수조사
for char in cal:
    # 연산자라면
    if char in '+-*/()':
        # print(char, '연산자')
        # 연산자 우선 순위에 맞춰서 stack 넣거나 뺴거나
        # 우선 순위가 높은 순으로 조건문 처리
        if char == '(':
            stack.append(char)   # 우선순위 제일 높으므로 그냥 push
        elif char in '*/':  # 마지막 값이 나와 같은 */ 일떄까지
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    else:
        # 정수면 result에 더해버리면된다.
        result += char
    print(result, stack)
while stack:
    result += stack.pop()
print(result, stack)