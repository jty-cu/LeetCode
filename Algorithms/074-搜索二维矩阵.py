class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ## 通过一维坐标访问二维数组
        def get(index):
            i = index // n
            j = index % n
            return matrix[i][j]
        left, right = 0, m*n-1
        while left <= right:
            mid = left + (right - left) // 2
            val = get(mid)
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid -1
        return False