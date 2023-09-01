n= int(input())

li= list(map(int,input().split()))

stack =[]
result=[0]*n

for i in range(n-1,-1,-1):
    while stack and li[stack[-1]] < li[i]:
        result[stack.pop()]= i+1
    stack.append(i)

print(*result)
