class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, sum0, start):
            nonlocal res
            if sum0 == target:
                res.append(track[:])
                return
            if sum0 > target:
                return
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                sum0 += candidates[i]
                dfs(candidates, target, sum0, i)## 多加一个分支，保证该数值还是可以选择
                track.pop()
                sum0 -= candidates[i]
        res, track = list(), list()
        sum0 = 0
        dfs(candidates, target, sum0, 0)
        return res
