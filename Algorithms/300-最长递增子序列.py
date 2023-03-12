'''
DP的定义：以nums[i]为结尾的最长递增子序列的个数
dp[i]的更新逻辑：遍历j<i, if nums[j]<nums[i], dp[i] = max(dp[i], dp[j]+1)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])
        return res