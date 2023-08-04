N = int(input())
my_list= list(map(int, input().split()))
v= int (input())

cnt = 0

for i in range(N):
    if my_list[i] == v:
        cnt +=1
        

print(cnt)    
