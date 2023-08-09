def fibo(n):
    global cnt
    cnt += 1
    print(cnt)
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
cnt = 0
result = []
print(fibo(100))
print(cnt)