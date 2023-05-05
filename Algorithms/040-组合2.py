'''
que: sum0为什么要作为参数传进来
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        sum0 = 0
        res, track = list(), list()
        def backtrack(start, sum0, target):
            nonlocal res
            if sum0 == target:
                res.append(track[:])
            if sum0 > target:
                return #??
            for i in range(start, n):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                sum0 += candidates[i]
                track.append(candidates[i])
                backtrack(i+1, sum0, target)
                sum0 -= candidates[i]
                track.pop()
        backtrack(0, sum0, target)
        return res