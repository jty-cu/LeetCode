# dp[i]: 以nums[i]为结尾的上升序列的长度
# dp[i] = max(dp[j]+1), when 0<=j<i and nums[j]<nums[i]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
            
