class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, used, track):
            nonlocal res
            ## 结束条件
            if len(track) == len(nums):
                res.append(track[:]) ## 深拷贝
            ## backtrack
            for i in range(len(nums)):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums, used, track)
                track.pop()
                used[i] = False
        res = list()
        used = [False for _ in range(len(nums))]
        track = list()
        backtrack(nums, used, track)
        return res