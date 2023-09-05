n ,m = map(int, input().split())
li=[]

for i in range(1,n+1):
    li.append(i)


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

