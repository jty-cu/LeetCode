class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        ## base case
        dp[0][1] = -prices[0]

        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i-1])
        return dp[n][0]

## 压缩维度
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(n):
            tmp = dp0 ## 这里需要用tmp记录dp0 / dp1的值（看执行顺序），因为先执行的值会被覆盖掉
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, tmp-prices[i])
        return dp0