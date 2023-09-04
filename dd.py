string = input()

stack=[]
result=''

for i in string:
    if i.isalpha:
        result+=i

    else:
        if not stack:
            stack.append(i)

        else:
            if i== '(':
                stack.append(i)

            elif i ==')':
                while         
