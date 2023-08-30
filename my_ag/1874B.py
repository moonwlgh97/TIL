n = int(input())

stack = []
result = []
now = 1
find = True

for _ in range(n):
    num= int(input())

    while now <= num:
        stack.append(now)
        result.append('+')
        now+=1

    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        find= False

if find==False:
    print('NO')

else:
    for i in range(len(result)):
        print(result[i])


