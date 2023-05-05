class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        ## dfs的作用是淹没岛屿，FloodFill算法
        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n:
                return 
            if grid[i][j] == '0':
                return 
            ## 发现一个岛屿，淹没
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    ## 然后淹没岛屿
                    dfs(i, j)
                # dfs(i, j) ##放这里可以跑过，但是这个意味着不管是不是陆地，我们每次都会淹没，但是实际上我们只要淹没岛屿，增加了时间复杂度
        return res




