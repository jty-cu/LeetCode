
'''
dp[i][j]: 从(0,0)到(i,j)的最小路径和(i表示行)
目标: dp[n-1][:]中的最小值
状态转移方程：dp[i,j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):  ## 注意起始值
            nums = triangle[i]
            for j in range(len(nums)):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + nums[j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + nums[j]

        res = float("inf")
        for i in range(len(dp[n - 1])):
            res = min(res, dp[n - 1][i])
        return res


## 空间优化算法怎么做