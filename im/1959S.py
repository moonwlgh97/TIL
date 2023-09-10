T= int(input())

for tc in range(1,T+1):
    n,  m = map(int, input().split())
    A= list(map(int, input().split()))
    B= list(map(int, input().split()))


    if n>m:
        n,m = m,n
        A,B= B,A

    result=0

    for i in range(m-n+1):
        temp=0
        for j in range(n):
            temp+= A[j]*B[j+i]

        if result < temp:
            result=temp


    print(f'#{tc} {result}')


