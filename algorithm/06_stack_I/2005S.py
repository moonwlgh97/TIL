T = int(input())
n = int(input())

for tc in range(1, T+1):
    pascal = [[0]*n for _ in range(n)]
    pascal[0][0] =1
    print(f'{tc}')
    for i in range(1, n):
        for j in range(n):
            if j ==0:
                pascal[i][j] = 1
            else:
                pascal[i][j]= pascal[i-1][j-1]+pascal[i-1][j]

            if pascal[i][j]:
    
                print(pascal[i][j], end = ' ') 
        print()               