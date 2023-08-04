# 시간 정수 입력 받기
# H 시간, M 분

H, M = map(int, input().split())


if M >= 45:
    print(H,M-45)
elif H > 0 and M < 45:
    print(H - 1, M  + 15)
else:
    print(23, M + 15)        