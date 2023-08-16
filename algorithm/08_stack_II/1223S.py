for tc in range(1,11):
    n = int(input())
    s= list(input())
    stack =[]
    result= []

    for i in s:
        if i.isdigit():
            result.append(i)

        else:
            if i =='*':
                while stack and stack[-1]=='*':
                    result.append(stack.pop())
                stack.append(i)

            elif i =='+':
                while stack:
                    result.append(stack.pop())
                stack.append(i)

    while stack:
        result.append(stack.pop())



    for i in result:
        if i not in '+*':
            stack.append(int(i))

        else:
            b=stack.pop()
            a=stack.pop()

            if i =='*':
                stack.append(a*b)

            elif i =='+':
                stack.append(a+b)

    print(f'#{tc} {stack[-1]} ')                

                
        

    