st = input()
calpha=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in calpha:
    st = st.replace(i,"*")
print(len(st))   