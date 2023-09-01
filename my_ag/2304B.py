n= int(input())

pillar= [0]*1001
max_h=0
max_idx=0


for _ in range(n):
    L, H= map(int,input().split())
    pillar[L]=H
    if max_h < H:
        max_h=H
        max_idx=L

curr = 0
result=0
# 왼쪽
for i in range(max_idx+1):
    curr=max(curr,pillar[i])
    result+=curr

#오른쪽
curr1=0
for i in range(1000,max_idx,-1):
    curr1=max(curr1,pillar[i])
    result+=curr1

print(result)
