# 动态规划

rnums = int(input())
pos = list(map(int,input().split()))

dp = [0]*(rnums+1)
for i in range(1,rnums+1):
    dp[i] = 2*dp[i-1]-dp[pos[i-1]-1]+2
    dp[i] = dp[i]%(1000000007)
print(dp[-1])
