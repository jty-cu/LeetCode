'''
打家劫舍问题1 的变形
考虑[0, n-2] 和 [1, n-1]的情况，每种情况都和问题1等价

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums, start, end):2
            dp1 = 0
            dp2 = 0
            dp = 0
            for i in range(end, start-1, -1):
                ## dp[i] = max(dp[i+1], dp[i+2]+nums[i])
                ## ----+----+----
                ##  dp +dp1 +dp2
                ## ----+----+----
                ## 移动顺序就是 dp-->dp1, dp1-->dp2所有的往前移动一个位置去计算下一个dp
                dp = max(dp1, dp2+nums[i])
                dp2 = dp1
                dp1 = dp
            return dp
        n = len(nums)
        if n==1: return nums[0]
        res = max(robRange(nums, 0, n-2), robRange(nums, 1, n-1))
        return res