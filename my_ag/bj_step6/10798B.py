import sys
input = sys.stdin.readline
a=[]
for i in range(5):
    a.append(list(input().strip()))
li1=[]

for i in range(5):
    li1.append(len(a[i]))


for i in range(max(li1)):
    for j in range(5):
         if len(a[j]) <= i: 
             pass
         else:
            print(a[j][i],end="")

        

  
