import sys
input = sys.stdin.readline

n, m = map(int, input().split())
my_list = list(map(int, input().split()))
sum_list = [0]
temp =0

for i in my_list:
    temp =temp +i
    sum_list.append(temp)



for _ in range(m):
    i, j = map(int, input().split())
    

    print(sum_list[j] - sum_list[i-1])    
