'''
Floodfilled算法
其他问题的变形：一般就是考虑
(a)如何淹没多余的岛屿 【边界的岛屿、子岛屿】
(b) 如何在dfs中统计不同的内容【岛屿个数、岛屿面积、岛屿形状】
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            m, n = len(grid), len(grid[0])
            ## 边界超出索引
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            ## 已经是海水
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            ## 淹没上下左右的陆地 ** 重要 **
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                dfs(grid, i, j)
        return res