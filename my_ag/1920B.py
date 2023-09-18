import sys
sys.setrecursionlimit(100000)


def binary_search(target):
    low= 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if a[mid] == target:
            return 1
            
        
        elif a[mid] < target:
            low = mid+1

        else:
            high = mid-1

    return 0            




n = int(input())
a =sorted(list(map(int, input().split())))
m= int(input())
b = list(map(int, input().split()))

for i in range(m):
    binary_search(b[i])
    if binary_search(b[i]) ==1:
        print(1)
    else:
        print(0)    

