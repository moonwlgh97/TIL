my_list = []
max = 0

for i in range(9):
    a = int(input())
    my_list.append(a)
    

    for j in range(len(my_list)):
        if my_list[j] > max:
            max = my_list[j]
print(max)
print(my_list.index(max)+1)


  
