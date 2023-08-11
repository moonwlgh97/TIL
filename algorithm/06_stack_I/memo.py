import sys
sys.setrecursionlimit(3000)

def fibo1(n):
    global memo, cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:  # 2 이상인데 아직 계산된 적이 없으면(아직 채워진 적이 없으면)
        memo[n] = (fibo1(n-1) + fibo1(n-2)) # 걔는 계산해서 memo[n]에다가 저장하고
    return memo[n]  # 저장된 값을 돌려줘 / if만족안하면 이미 계산되어있는 값을 돌려줄게
cnt = 0
n = 1000
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
fibo1(n)
print(memo[-1])
print(cnt)