class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]

        ## base case
        for i in range(0, m):
            dp[i][0] = int(matrix[i][0])
        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        ## calc max square
        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dp[i][j])
        return max_len**2