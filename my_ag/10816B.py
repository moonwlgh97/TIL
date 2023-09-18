import sys
input= sys.stdin.readline

def binary_search(target):
    low = 0
    high = n-1
   

    while low <= high:
        mid = (low+high)//2

        if a[mid] == target:
           return a[low:high+1].count(target)
            
        elif a[mid] < target:
            low = mid +1

        else:
            high = mid -1

    return 0             




n = int(input())
a = sorted(list(map(int, input().split())))
m= int(input())
b= list(map(int,input().split()))



for i in range(m):
   print(binary_search(b[i]), end=' ')
   