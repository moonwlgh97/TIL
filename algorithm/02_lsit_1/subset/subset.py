numbers=[-7, -3, -2, 5, 8]
N=5


#numbers로 만들 수 있는 모든 경우의 수
# 1<<N == 2**N
# 1왼쪽으로 3번 쉬프트한다
#0001 -> 1000
for x in range(1<<N): # 100000
    result = 0
    subset= []
    # 그모든 경우의 수에서
    # numbers의 y번째 요소가
    # x번 경우의 수에 사용되었는지를 판별
    # x번 경우의 수가 1일때 bit는 -> 0001
    # numbers의 y번째 요소(0번째 요소) -> 0001
    #numbers의 0번째 요소가 0001 -> (1<<0)
    #numbers의 1번째 요소가 0010 -> (1<<1)
    for y in range(N):
        if x & (1<<y):
            result += numbers[y]
            subset.append(numbers[y])

    if len(subset) ==2 and '미나리' not in subset:
        print(subset)
    if result ==0:
        print(1)
        break
