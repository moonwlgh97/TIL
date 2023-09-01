import sys
n= int(input())
li= list(map(int, input().split()))
stack=[]
result=[-1]*n
for i in range(n):
    while stack and li[stack[-1]] < li[i]:
        result[stack.pop()]=li[i]
    stack.append(i)

print(*result)
