n,m= map(int, input().split())

li=[]

for i in range(1,n+1):
    li.append(i)


stack=[]

def back():
    if len(stack) == m:
        print(*stack)
        return
    
    for i in li:
        if not stack:
            stack.append(i)
            back()
            stack.pop()
        else:
            if stack[-1] <=i:
                stack.append(i)
                back()
                stack.pop()

back()                    