string = input()

stack=[]
result=[]

for i in string:
    if i.isdigit():
        result.append(i)

    else:
        if not stack:
            stack.append(i)

        else:
            if i =='(':
                stack.append(i)

            elif i ==')':
                while stack[-1] !='(':
                    result.append(stack.pop())
                stack.pop()

            elif i=='*' or i=='/':
                while stack and stack[-1]=='*' or stack[-1]=='/':
                    result.append(stack.pop())
                stack.append(i)


            elif i =='+' or i=='-':
                while stack and stack[-1] !='(':
                    result.append(stack.pop())

                stack.append(i)

while stack:
    result.append(stack.pop())


print(*result)
