## 遇到障碍直接跳过
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        ## base case
        dp[1][1] = 1 if obstacleGrid[0][0]==0 else 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


## 空间优化
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*(n+1)
        ## base case
        dp[1] = 1 if obstacleGrid[0][0]==0 else 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i ==1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    dp[j] = 0
                    continue
                dp[j] = dp[j] + dp[j-1] ## 如果不考虑第二个if中的dp[j]更新，那dp[j]表示第i-1行时，到j列的路有多少条；dp[j-1]表示第i行时，到j-1的路有多少条
        return dp[-1]




