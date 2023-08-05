n = int(input())

li = list(map(int,input().split()))
new_list = []
max_s = max(li)

for score in li:
    new_list.append(score/max_s * 100)

print(sum(new_list)/n)    
