# 이진검색 - 재귀호출
arr = [2, 4, 7, 9, 11, 19, 13]
# 정렬을 무조건 해야함
arr.sort()

# 함수 한 번 호출 때 마다 low, high 변수가 바뀌어서 사용됨
def binarySearch(low, high, target):

    # 데이터를 못 찾을때
    if low > high:
        return -1

    mid = (low+high) //2
    #1. 가운데 값이 정답인 경우
    if target== arr[mid]:
        return mid

    #2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid+1, high, target)
    
    #3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid-1, target)
