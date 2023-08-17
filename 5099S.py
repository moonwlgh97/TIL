from collections import deque


n,m = map(int, input().split()) # 화덕크기 , 피자개수
pizza = deque(list(map(int, input().split())))
fire = deque()

if len(fire) <3:
    for i in range(n):
        fire.append(pizza.popleft())

else:
    cnt = 0
    while fire:
        a= fire.popleft()
        fire.append(a)
        cnt+=1

        if cnt%n ==0:
            for i in range(n):
                a = fire[i]//2
                fire[i]=a

                print(fire)















