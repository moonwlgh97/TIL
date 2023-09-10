n = int(input())
li = list(map(int, input().split()))
k_li=[]

for k in range(n):

    for i in range(k):
        for j in range(i+1,k):
            if li[k] == li[i]+li[j]:
                k_li.append(li[k])

print(len(set(k_li)))