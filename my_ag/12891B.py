checkList =[0]*4
my_list = [0]*4
checkSecret = 0

def myadd(c):
    global checkList, my_list, checkSecret
    if c == 'A':
        my_list[0]+=1
        if my_list[0]==checkList[0]:
            checkSecret +=1
    elif c == 'C':
        my_list[1]+=1
        if my_list[1]==checkList[1]:
            checkSecret +=1
    elif c == 'G':
        my_list[2]+=1
        if my_list[2]==checkList[2]:
            checkSecret +=1
    elif c == 'T':
        my_list[3]+=1
        if my_list[3]==checkList[3]:
            checkSecret +=1                

def myremove(c):
    global checkList, my_list, checkSecret
    if c =='A':
        if my_list[0] == checkList[0]:
            checkSecret -=1
        my_list[0] -=1
    if c =='C':
        if my_list[1] == checkList[1]:
            checkSecret -=1
        my_list[1] -=1
    if c =='G':
        if my_list[2] == checkList[2]:
            checkSecret -=1
        my_list[2] -=1
    if c =='T':
        if my_list[3] == checkList[3]:
            checkSecret -=1
        my_list[3] -=1


s, p = map(int, input().split())
result = 0
a = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] ==0:
        checkSecret+=1
for i in range(p):
    myadd(a[i])
    if checkSecret ==4:
        result +=1

for i in range(p,s):
    j = i-p
    myadd(a[i])
    myremove(a[j])
    if checkSecret==4:
        result +=1
print(result)        


                
                            

