
arr = [2, 4, 7, 9, 11, 19, 13]
# 정렬을 무조건 해야함
arr.sort()

def binarySearch(target):
    low =0
    high= len(arr) -1

    # low > high라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) //2

        # 가운데 값이 정답인 경우
        if arr[mid]==target:
            return mid
        # 가운데 값이 정답보다 작은경우
        elif arr[mid] < target:
            low = mid+1
        # 가운데 값이정답보다 큰 경우
        else:
            high= mid -1

    # 해당데이터를 찾지 못한 경우우
    return -1