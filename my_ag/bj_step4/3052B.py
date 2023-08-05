li = []

for _ in range(10):
    i= int(input())
    if i%42 not in li:
        li.append(i%42)

print(len(li))        