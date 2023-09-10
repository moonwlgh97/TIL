for tc in range(1,11):

    dump = int(input())
    li= list(map(int, input(). split()))
    
    

    for _ in range(dump):
      li_max=max(li)
      li_min=min(li)

      max_idx = li.index(li_max)
      min_idx = li.index(li_min)

      li[max_idx] -=1
      li[min_idx] +=1
    
    print(f'#{tc} {max(li)-min(li)}')    

    