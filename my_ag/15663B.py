n ,m = map(int, input().split())
li=list(map(int,input().split()))
li.sort()
stack=[]

def back():
    if len(stack) ==m:
        for i in stack:
            print(li[i], end=' ')
        print()
        return
    pre=0
    for i in range(len(li)):
        if not stack and pre != li[i]:
            stack.append(i)
            pre=li[i]
            back()
            stack.pop()


        if i not in stack and pre != li[i] and li[stack[-1]] <= li[i]:
            stack.append(i)
            pre=li[i]
            back()
            stack.pop()

back()