import sys

sys.stdin = open('input.txt')


def cal(word, stack):
    for char in word:
        # 현재 조사 대상이 연산자가 아니면
        if char not in '*/+-':
            # 스택에 추가
            stack.append(int(char))
        else:
            # 스택에서 값 2개 제거
            # 만약 후위표기식이 잘못 되었다면, 연산 불가능
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
    return stack[-1]


for tc in range(1, 11):
    N = int(input())
    word = input()
    stack = []
    result = ''

    for char in word:
        # 현재 조사 대상이 연산자일 때,
        if char in '*+':
            # 스택이 비었다면
            if not stack:
                # 우선 삽입
                stack.append(char)
            # 스택에 값이 있고,
            # 조사 대상이 곱셈의 경우
            elif char in '*':
                # 스택에 값이 남아 있고
                # 스택의 마지막이 곱셍인 동안
                while stack and stack[-1] == '*':
                    # 최종 후위표기값에 곱셈 추가 + 스택에서 제거
                    result += stack.pop()
                # 처리 완료 후, 스택의 현재 곱셈 다시 추가
                stack.append(char)
            # 덧셈인 경우
            elif char in '+':
                # 스택을 모두 비울때까지
                while stack:
                    # 스택에서 요소 제거
                    result += stack.pop()
                # 처리 완료 후, 스택에 덧셈 추가
                stack.append(char)
        # 연산자가 아닌경우,
        else:
            # 최종 후위표기값에 값 추가
            result += char

    # 모든 처리 후에도 스택이 남았다면
    while stack:
        # 값 추가
        result += stack.pop()

    # 계산 시작
    result = cal(result, [])

    print(f'#{tc} {result}')