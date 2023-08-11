import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    # print(word)
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    # print(stack)
    print(f'#{tc} {len(stack)}')