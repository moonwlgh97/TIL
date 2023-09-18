def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left, right = [], []
        for i in range(1,len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])

        return [*quick_sort(left), pivot, *quick_sort(right)]

nums = [23, 12, 60, 77, 32, 1]
print(quick_sort(nums))

