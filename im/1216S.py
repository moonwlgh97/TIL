for _ in range(1,11):
    tc = int(input())


    li=[list(map(str,input())) for _ in range(100)]
    max_len=0
    max =0
    max1=0
    
    for n in range(1,100):
         
         for i in range(100):
            fel=[]
            fel1=[]
            for j in range(100):
                fel.append(li[i][j])
                fel1.append(li[j][i])

                if len(fel)==n:
                    if fel==fel[::-1]:
                        max=len(fel)
                        fel.pop(0)
                    else:
                        fel.pop(0) 

                if len(fel1)==n:
                    if fel1 == fel1[::-1]:
                        max1=len(fel1)
                        fel1.pop(0)
                    else:
                        fel1.pop(0)    
    if max1>max:

        print(f'#{tc} {max1}')

    else:
         print(f'#{tc} {max}')                        

