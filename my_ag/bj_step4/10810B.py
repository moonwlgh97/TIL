
N, M = map(int, input().split())

my_list = [0] *(N+1)

for _ in range(M):
    i,j,k = map(int, input().split())
    for num in range(i, j+1):
        my_list[num] = k
for i in range(1, N+1):
    print(my_list[i], end=' ')    