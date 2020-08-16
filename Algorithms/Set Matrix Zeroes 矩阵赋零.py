# 找相应的行和列
# 赋零

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # row
        m = len(matrix[0]) # col
        
        # zeroRow = zeroCol = [] # 这会使得下面zeroRow == zeroCol
        zeroRow = []
        zeroCol = []
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroRow.append(i)
                    zeroCol.append(j)
        
        #zeroRow = set(zeroRow)
        #zeroCol = set(zeroCol)
        
        for z in zeroRow:
            for i in range(m):
                matrix[z][i] = 0
            
        for z in zeroCol:
            for i in range(n):
                matrix[i][z] = 0
