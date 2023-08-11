import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    k = int(input())

    if k == 0:
        stack.pop()

    else:
        stack.append(k)

print(sum(stack))            
    
