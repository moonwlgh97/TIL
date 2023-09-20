def back(start):
    global cnt
    if sum(stack) == 0 and len(stack) >0:
        cnt +=1

    for i in range(start,n):
        stack.append(i)
        back(i+1)
        stack.pop()

n, s = map(int, input().split())
li= list(map(int, input().split()))
stack = []
cnt =0

back(0)
print(cnt)