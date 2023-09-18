T= int(input())
def binarysearch(target):

    low =0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if a[mid] == target:
            return 1

        elif a[mid] < target:
            low = mid+1

        else:
            high = mid -1
    return 0




for tc in range(1, T+1):
    n,m = map(int,input().split())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    cnt=0

    a.sort()

    for i in b:
        if binarysearch(i)==1:
            cnt+=1


    print(f'#{tc} {cnt}')

