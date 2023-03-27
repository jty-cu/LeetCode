## 问题重构
'''
本质上是一个组合问题，现在有2n个位置，可以怎么样放置括号。哪些放置是合法的
组合问题 --> 回溯
判断是否合法的过程可以看成是剪枝
合法的括号的定义
1. 左括号数量 = 右括号数量
2. 对于任何一个子串，左括号数量 >= 右括号数量
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        track = ""

        def backtrack(track, left, right):
            '''
            left: 可用的左括号数量
            '''
            nonlocal res
            ## 剪枝
            if left > right:  ## 剩余括号左>右，不合法
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(track)
                return

            track += '('
            backtrack(track, left - 1, right)
            track = track[:-1]

            track += ')'
            backtrack(track, left, right - 1)
            track = track[:-1]

        backtrack(track, n, n)
        return res

