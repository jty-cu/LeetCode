## 和lc200的岛屿问题很类似
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        found = False
        def dfs(i, j, p):
            nonlocal found
            if p == len(word):
                found = True
                return
            if found:
                return
            ## 超边界
            if i<0 or j<0 or i>=m or j>=n:
                return
            ## 不匹配
            if board[i][j] != word[p]:
                return
            ## 匹配
            ## 打标，避免走回头路
            board[i][j] = board[i][j]+"0"
            dfs(i-1, j, p+1)
            dfs(i+1, j, p+1)
            dfs(i, j-1, p+1)
            dfs(i, j+1, p+1)
            board[i][j] = board[i][j][0]
        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
                if found:
                    return True
        return False
