T = int(input())

for tc in range(1, T+1):
    stack = []
    s = input()+'0'

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            stack.append(s[i])
            for _ in range(len(stack)):



    print(len(stack))


