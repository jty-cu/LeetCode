## 数组；技巧型
'''
不断更新4个边界
1. while 条件
2. 更新时， i, j移动的方向
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        m = len(matrix)
        n = len(matrix[0])
        upper = 0
        lower = m-1
        left = 0
        right = n-1
        while len(res) < m*n:
            if upper <= lower:
                for j in range(left, right+1): ## zhuyi: right+1
                    res.append(matrix[upper][j])
                upper += 1

            if left <= right:
                for i in range(upper, lower+1):
                    res.append(matrix[i][right])
                right -= 1

            if upper <= lower:
                for j in range(right, left-1, -1): ## zhuyi: right+1
                    res.append(matrix[lower][j])
                lower -= 1

            if left <= right:
                for i in range(lower, upper-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res