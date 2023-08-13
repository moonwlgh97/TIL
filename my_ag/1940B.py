n= int(input())
sum_n= int(input())
n_li = list(map(int, input().split()))

cnt = 0

for i in range(n):
  s= 0
  
  for j in range(i+1,n):
    s= n_li[i]+n_li[j]
    
    if s== sum_n:
      cnt +=1
      
    
print(cnt)    
       
      




    

