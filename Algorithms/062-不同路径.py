## 注意起始条件，都是1
## 和走几步和路径分开来，如果是记录路径的条数，就是dp，如果是记录路径，就是backtrack
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = list()
        dp = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(0, m):
        #     dp[i][0] = 1
        # for j in range(0, n):
        #     dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]