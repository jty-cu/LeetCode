class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(m + 1)]
        ## base case
        ## dp[i][0] = 1, dp[0][i] = 0
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[-1][-1]

'''
压缩维度
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(m):
            for j in range(1, amount+1): ## 注意更新顺序
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]] ## 需要依赖更新后的dp[j-coins[i]]
        return dp[-1]