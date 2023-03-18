'''
dp[i][k][..] 不会依赖 dp[i][k - 1][..]，而是依赖 dp[i - 1][k - 1][..]，
而 dp[i - 1][..][..]，都是已经计算出来的，所以不管你是 k = max_k, k--，
还是 k = 1, k++，都是可以得出正确答案的。

那为什么我使用 k = max_k, k-- 的方式呢？因为这样符合语义：
你买股票，初始的「状态」是什么？应该是从第 0 天开始，而且还没有进行过买卖，所以最大交易次数限制 k 应该是 max_k；
而随着「状态」的推移，你会进行交易，那么交易次数上限 k 应该不断减少，这样一想，k = max_k, k-- 的方式是比较合乎实际场景的。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp = [[[0 for _ in range(2)] for _ in range(max_k+1)] for _ in range(n)]

        for i in range(n):
            # for k in range(1, max_k+1): ## 注意遍历顺序和下标，k=0的情况不考虑，因为不交易收益就是0，就是默认的dp[..][k][..]
            for k in range(max_k, 0, -1): ## 两种都可以
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][max_k][0]
        # return dp


## 压缩空间
'''
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1]+prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0]-prices[i])
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
            = max(dp[i-1][1][1], -prices[i])

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp10, dp11 = 0, -prices[0]
        dp20, dp21 = 0, -float('inf')
        for i in range(n):
            ## 注意更新顺序
            dp20 = max(dp20, dp21+prices[i])
            dp21 = max(dp21, dp10-prices[i])
            dp10 = max(dp10, dp11+prices[i])
            dp11 = max(dp11, -prices[i])
        return dp20