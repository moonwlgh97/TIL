N = int(input())
my_list = list(map(int, input().split()))

max = my_list[0]
min = my_list[0]

for i in range(N):
    if my_list[i] > max:
        max = my_list[i]

    elif my_list[i] < min:
        min = my_list[i]

print(min, max)            