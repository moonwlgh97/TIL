


q = []

result = []

n, k = map(int, input().split())

for i in range(1,n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.pop(0))
    result.append(q.pop(0))

print('<', end='')
print(', '.join(map(str, result)), end='')
print('>')


# join 알아보기