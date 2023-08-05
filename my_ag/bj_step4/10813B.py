N, M =map(int, input().split())

my_list=[0]*(N+1)
 
for num in range(1,N+1):
    my_list[num] = num

for _ in range(M):
    i, j = map(int, input().split())
    
    my_list[i], my_list[j] = my_list[j], my_list[i]


for i in range(1,N+1):
    print(my_list[i], end=" ")
   



   
