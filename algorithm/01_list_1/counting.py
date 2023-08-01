# 매개 변수가 2개 필요하다
# 입력배열 : numbers
# numbers가 가진 최대 정수 값 :k

def counting_sort(numbers,k):

    count_arr = [0]*(k+1)
    # 최종 정렬 된 값을 담을 배열
    # result의 범위 : numbers의 전체 원소 양 만큼
    result = [-1]*len(numbers)


    for i in range(len(numbers)):
        count_arr[numbers[i]] += 1
    print(count_arr)

    # 각 요소가 들어있는 개수를 확인 했으니..
    # 각 요소가 들얻가야 할 인덱스를 계산하기위해
    # 누적 값 카운팅
    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    print(count_arr)

    #원본배열의 값들을 다시 순회하면서
    # 원본 배열의 각 값들을 정렬 된 인덱스 위치에 담아주기
    for num in numbers:
        count_arr[num] -=1
        result[count_arr[num]] = num
    return result







numbers=[0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(numbers,5))





