T= int(input())

for tc in range(1,T+1):
    n= int(input())
    li= list(map(int,input()))
    li.sort()

    result_max=0

    num_idx=[0]*10

    for i in li:
        num_idx[i] +=1

    for i in range(len(num_idx)):
        if num_idx[i] >= result_max:
            result_max= num_idx[i]
            result_idx= i


    print(f'#{tc} {result_idx} {result_max}')