# 2 + 3 * 4 / 5

cal = '2+3*4/5'
# 최종 결괏값
result = '' # 피연산자 + 연산자
# 연산자들을 모아 둘 stack
stack = []

# 전수조사
for char in cal:
    # 연산자가 아닌경우 (정수 인경우)
    if char not in '+-*/':
        result += char
    else:
        stack.append(char)
# stack에 들어있는 모든 연산자들을 result에 더해주려면
while stack:
    result += stack.pop()
print(result, stack)
