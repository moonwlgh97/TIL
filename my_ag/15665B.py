n,m=map(int, input().split())
li= list(map(int, input().split()))
li.sort()
stack=[]


def back():
    if len(stack)==m:
        print(*stack)
        return
    pre=0
    for i in li:
        if pre != i:
            stack.append(i)
            pre = i
            back()
            stack.pop()
back()