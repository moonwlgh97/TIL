dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV','WXYZ']
word = input()
sum = 0
for x in dial:
    for y in x:
        for z in word:
            if z == y:
                sum = sum+dial.index(x) +3

print(sum)

