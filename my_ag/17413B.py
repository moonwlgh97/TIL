s = input()+ ' '
stack = []
result = ''
cnt = 0
for i in s:
    if i=='<':
        cnt =1
        for _ in range(len(stack)):
            result+=stack.pop()
    stack.append(i)

    if i == '>':
        cnt =0
        for _ in range(len(stack)):
            result +=stack.pop(0)

    if cnt ==0 and i ==' ':
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()

        result += ' ' 

print(result)                    
            


