import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input().split()

    stack = []
    # 연산자
    operator = '+-*/'
    result = 0
    # 숫자는 스택에 넣는다.
    for char in data:
        if char.isdecimal():
            stack.append(int(char))
        # 연산자를 만나면 스택의 숫자 두 개를 꺼내서
        # 연산을 위한 stack의 길이 확인
        elif char in operator and len(stack) >= 2:
            # stack = [4, 2] 일 때, 나눗셈은 4//2 여야 하므로
            # stack의 마지막 요소를 임시 변수에 담아두고
            x = stack.pop()
            y = stack.pop()
            # 연산을 한 후
            # 결과를 다시 스택에 넣는다
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            else:
                stack.append(y // x)
        # 입력된 값이 . 이고, 남은 stack이 1개이면 pop
        elif char == '.' and len(stack) == 1:
            result = stack.pop()
        # 연산자를 만났으나, stack이 2개 미만이면 break
        elif char in operator and len(stack) < 2:
            result = 'error'
            break
        # 입력된 값이 .인데, 남은 stack이 2개 이상이면 error
        elif char == '.' and len(stack) > 2:
            result = 'error'
            break


    print(f'#{tc} {result}')
