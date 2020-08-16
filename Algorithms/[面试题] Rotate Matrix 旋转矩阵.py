# 转置
# 处理行

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(n-i):
                matrix[i][j],matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1],matrix[i][j]
                
        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
