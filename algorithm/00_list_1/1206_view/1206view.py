import sys
sys.stdin = open('input.txt')
T= 10

for tc in range(1, T+1):
     tc_len = int(input())
     bh = list(map(int, input().split()))

     result = 0 # 조망권이 확보된 세대수

     for i in range(2, tc_len-2):
         if bh[i] > bh[i-1] and bh[i]> bh[i-2] and bh[i]>bh[i+1] and bh[i]>bh[i+2]:
             max_h = bh[i-2]
             # 비교하는 4개의 건물 중 가장 높은 값을 구하기 위해 변수를 초기화

             for j in range(-2,3):
                 if j==0:
                     continue
                 if bh[i-j] > max_h:
                     max_h = bh[i-j]
             result += bh[i] - max_h
     print(f'#{tc} {result}')










