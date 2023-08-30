T= int(input())

for _ in range(T):
    string = input()+' '
    stack = []
    result= []
    for i in string:
        stack.append(i)
        if i==' ':
            while stack:
                result.append(stack.pop())
    while stack:
        result.append(stack.pop())
    result.pop(0)
    print(''.join(result))



    # 다른 풀이
    # N= int(input())
    #
    # for i in range(N):
    #     string = list(input().split())
    #     for j in string:
    #         print(j[::-1], end=' ')


