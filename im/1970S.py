T= int(input())

for tc in range(1,T+1):
    print(f'#{tc}')
    money= int(input())
    won_check=[0]*8

    if money >=50000:
        a=money//50000
        money= money-(a*50000)
        won_check[0]+=a


    if money >= 10000:
        a = money // 10000
        money = money - (a * 10000)
        won_check[1] += a

    if money >=5000:
        a=money//5000
        money= money-(a*5000)
        won_check[2]+=a

    if money >=1000:
        a=money//1000
        money= money-(a*1000)
        won_check[3]+=a

    if money >= 500:
        a = money // 500
        money = money - (a * 500)
        won_check[4] += a

    if money >= 100:
        a = money // 100
        money = money - (a * 100)
        won_check[5] += a

    if money >= 50:
        a = money // 50
        money = money - (a * 50)
        won_check[6] += a

    if money >= 10:
        a = money // 10
        money = money - (a * 10)
        won_check[7] += a

    print(*won_check)



