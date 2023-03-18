class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            ## base case
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if i - 2 == -1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], -prices[i])
                continue
                ## dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i]) = max(dp[0][1], dp[-1][0]-prices[i]) = max(dp[0][1], 0-prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[-1][0]


## 压缩维度
'''
为什么中间可以注释：
1. i-1==-1的情况，就是初值，已经赋予了(line 31: dp0, dp1 = 0, -prices[0])
2. i-2==-1的情况，dp_pre==0使得迭代逻辑可以写成和其他情况一样，可以合并写
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ## initialize
        dp0, dp1 = 0, -prices[0]
        dp_pre = 0 ## dp[i-2][0]
        for i in range(n):
            # if i - 1 == -1:
            #     dp0 = 0
            #     dp1 = -prices[i]
            #     continue
            # if i - 2 == -1:
            #     dp0 = max(dp0, dp1+prices[i])
            #     dp1 = max(dp1, dp_pre-prices[i])  ## dp1 = max(dp1, 0-prices[i]) 也可以通过，但是就不能合并写了
            #     continue
            tmp = dp0
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, dp_pre-prices[i])
            ## 别忘记更新dp[i-2]，变成股票卖出，i.e. dp0
            dp_pre = tmp
        return dp0

