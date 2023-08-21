T = int(input())

for tc in range(1,T+1):
    n = int(input())
    bus_stop= [0]*5001
    ans=[]

    for _ in range(n):
        ai,bi= map(int, input().split())

        for i in range(ai,bi+1):
            bus_stop[i]+=1


    p = int(input())

    for _ in range(p):
        x = int(input())

        ans.append(bus_stop[x])

    print(f'#{tc}', end=' ')
    for i in ans:
        print( i,end=' ')
    print()    

                      


    