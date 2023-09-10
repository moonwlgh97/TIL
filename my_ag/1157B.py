st = input().lower()

st_list = list(set(st))

st_count = []

for i in st_list:
    st_count.append(st.count(i))

if st_count.count(max(st_count)) >=2:
    print('?')
else:
    print(st_list[st_count.index(max(st_count))].upper())    
