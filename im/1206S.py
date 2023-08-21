for tc in range(1,11):
     n= int(input())
     li=list(map(int, input().split()))
     ans=0

     for i in range(2,n-2):
          com=[]
          if li[i]>li[i-1] and li[i]>li[i-2] and li[i]>li[i+1] and li[i]>li[i+2]:
               h = li[i]
               com.append(li[i-1])
               com.append(li[i-2])
               com.append(li[i+1])
               com.append(li[i+2])
               h2=li[i-2]

               
               for j in com:
                    if h2< j:
                         h2= j

               ans= ans+(h-h2) 
          else:
               continue
          
     print(f'#{tc} {ans}')

                               

               
     
