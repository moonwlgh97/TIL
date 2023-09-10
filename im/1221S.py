T= int(input())

for _ in range(1, T+1):
    tc, n= input().split()
    print(f'{tc}')
    li=list(map(str, input().split()))

    new_li=[]


    num=['ZRO', 'ONE', 'TWO','THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT','NIN']

    for i in range(int(n)):
        new_li.append(num.index(li[i]))

    new_li.sort()

    for i in range(int(n)):
        new_li[i] = num[new_li[i]]

    print(*new_li)


