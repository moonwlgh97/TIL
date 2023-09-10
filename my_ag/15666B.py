n, m = map(int,input().split())
li=list(map(int,input().split()))
li.sort()
stack=[]

def back():
    if len(stack) == m:
        print(*stack)
        return
    pre=0
    for i in li:
        if not stack and pre != i:
            stack.append(i)
            pre=i
            back()
            stack.pop()
        else:
            if pre != i and stack[-1]<= i:
                stack.append(i)
                pre=i
                back()
                stack.pop()

back()


