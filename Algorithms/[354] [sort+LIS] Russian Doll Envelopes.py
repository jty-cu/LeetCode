# Since the width is increasing, we only need to consider height.
# [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key = lambda x:(x[0],-x[1]))
        nums = [x[1] for x in envelopes]
        
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
        
