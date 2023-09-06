n, m = map(int, input().split())
li=list(map(int, input().split()))
li.sort()

stack=[]
def back():
    if len(stack) == m:
        print(*stack)
        return

    for i in li:
        stack.append(i)
        back()
        stack.pop()

back()