## 数组；技巧型
## 链接：leetcode 54

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dummy = 1
        up = 0
        down = n-1
        left = 0
        right = n-1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        while dummy <= n*n:
            if up <= down:
                for j in range(left, right+1):
                    ans[up][j] = dummy
                    dummy += 1
                up += 1
            if left <= right:
                for i in range(up, down+1):
                    ans[i][right] = dummy
                    dummy += 1
                right -= 1
            if up <= down:
                for j in range(right, left-1, -1):
                    ans[down][j] = dummy
                    dummy += 1
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    ans[i][left] = dummy
                    dummy += 1
                left += 1
        return ans

