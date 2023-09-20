def back():
    if len(stack)==n:
        print(*stack)
        return

    for i in li:
        if i not in stack:
            stack.append(i)
            back()
            stack.pop()

n = int(input())
li = [i for i in range(1,n+1)]
stack = []
back()