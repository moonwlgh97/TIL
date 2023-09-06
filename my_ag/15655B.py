n ,m = map(int,input().split())
li = list(map(int, input().split()))
li.sort()
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
            if i not in stack and stack[-1] < i:
                stack.append(i)
                back()
                stack.pop()

back()