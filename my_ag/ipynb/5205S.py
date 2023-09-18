
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot=arr[0]
        left,pivot_list, right = [],[],[]

        for i in arr:
            if i > pivot:
                right.append(i)

            elif i == pivot:
                pivot_list.append(i)

            else:
                left.append(i)

        return [*quick_sort(left), *pivot_list,*quick_sort(right)]




T= int(input())

for tc in range(1, T+1):
    n = int(input())
    nums= list(map(int, input().split()))

    new_nums= quick_sort(nums)


    print(f'#{tc} {new_nums[(n//2)]}')
