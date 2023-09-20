def back():
    global ans
    if sum(visited) ==n:
        total = 0
        for i in range(n-1):
            total += abs(stack[i]-stack[i+1])

        if total > ans:
            ans =total

            return


    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            stack.append(li[i])
            back()
            stack.pop()
            visited[i]=0


n = int(input())
li = list(map(int, input().split()))
visited= [0] *n
stack=[]
ans =0

back()
print(ans)
