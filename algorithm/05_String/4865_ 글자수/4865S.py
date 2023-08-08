T = int(input())

for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = list(input())

    str1_cnt = [0]* len(str1)

    for i in range(len(str1)):
        for j in str2:
            if str1[i] == j:
                str1_cnt[i] += 1
    print(f'#{tc} {max(str1_cnt)}')