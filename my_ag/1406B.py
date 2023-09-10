import sys
string_l=list(input())
string_r=[]
n= int(input())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='P':
        string_l.append(command[1])

    elif command[0]=='L' and string_l:
        string_r.append(string_l.pop())

    elif command[0]=='D' and string_r:
        string_l.append(string_r.pop())

    elif command[0]=='B' and string_l:
        string_l.pop()

print(''.join(string_l +list(reversed(string_r))))

# insert , remover
# sys.stdin.readline 과 input 차이




