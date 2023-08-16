T = int(input())


for tc in range(1,T+1):
    stack = [] #피연산자 담을 스택
    s = (input().split())

    for i in s:

        if i.isdigit() == True:
            stack.append(int(i))


        elif i == '.':
                if len(stack) ==1:
                    print(f'#{tc} {stack[-1]}')
                else:
                    print(f'#{tc} error')
                    break
        else:
             if len(stack) < 2:
                 print(f'#{tc} error')
                 break
             else:
                op2 = stack.pop()
                op1 = stack.pop()

                if i == '+':

                    stack.append(op1+op2)

                elif i =='-':
                    stack.append(op1-op2)

                elif i =='/':
                    stack.append(op1//op2)

                elif i == '*':
                    stack.append(op1*op2)



