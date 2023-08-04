N ,X = map(int, input().split())
my_list = list(map(int, input().split()))


for i in range(N):
    if my_list[i] < X:
        print(my_list[i], end=' ')
