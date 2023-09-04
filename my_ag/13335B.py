n, w, l = map(int, input().split())
trucks= list(map(int, input().split()))

b=[0]*w
time=0

while b:
    time+=1
    b.pop(0)
    
    if trucks:
        if sum(b)+trucks[0] <=l:
            b.append(trucks.pop(0))
        else:
            b.append(0)

print(time)