N, M= map(int, input().split())
li = [i for i in range(1,N+1)]

for _ in range(M):
    i, j= map(int, input().split())

    temp= li[i-1:j]
    temp.reverse()
    li[i-1:j] = temp

for i in range(N):
    print(li[i], end= ' ')    