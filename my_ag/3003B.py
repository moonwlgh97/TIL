pi = [1,1,2,2,2,8]
my_pi = list(map(int,input().split()))
new_pi = []

for i in range(len(pi)):
    if pi[i] > my_pi[i]:
        new_pi.append(pi[i]-my_pi[i])
    elif pi[i] < my_pi[i]:
        new_pi.append(pi[i]-my_pi[i])
    else:
        new_pi.append(0)


for i in range(len(pi)):
    print(new_pi[i], end= " ")