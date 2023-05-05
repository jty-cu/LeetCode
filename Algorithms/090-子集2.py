class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, track = list(), list()
        n = len(nums)

        def backtrack(start):
            nonlocal res
            res.append(track[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:  ## 注意：i和start(起点下标)比较，相同元素跳过回溯
                    continue
                track.append(nums[i])
                backtrack(i + 1)
                track.pop()

        backtrack(0)
        return res
