'''
1. dp[i]: 从第 i 间房子开始抢劫，最多能抢到的钱为 x
2. dp[i] = max(dp[i+1], dp[i+2]+nums[i])
自底向上（从n开始），倒序进行
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+2)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2]+nums[i])
        return dp[0] ## 注意return