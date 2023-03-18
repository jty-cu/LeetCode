## solution 01: 寻找历史低点
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        res = 0
        for price in prices:
            res = max(res, price-minprice)
            minprice = min(minprice, price)
        return res


## solution 02: dp
## 2 dim
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        dp[0][1] = -prices[0] ## 注意初始值的设定

        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1], -prices[i-1]) ## dp[i-1][0]==0, 因为不涉及多次交易
        return dp[n][0]

## one dim
'''
压缩空间：因为在2维中，只涉及状态dp[i-1][0], dp[i-1][1]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]

        for i in range(n):
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, -prices[i])
        return dp0