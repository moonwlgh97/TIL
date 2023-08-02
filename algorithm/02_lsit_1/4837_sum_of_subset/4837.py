import sys
sys.stdin = open('input.txt')
T= int(input())
set_list = [i for i in range(1, 13)]


for tc in range(1,T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1<<len(set_list)):
        cnt = 0
        sum = 0
        for j in range(len(set_list)):
            if i & (1<<j):
                sum += set_list[j]
                cnt+=1
        if cnt ==N and sum == K :
            ans += 1
    print(f'#{tc} {ans}')



