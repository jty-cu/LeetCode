## dp
## dp[i] = max(nums[i], dp[i-1]+nums[i])

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [-float('inf')]*len(nums)
#         dp[0] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(nums[i], dp[i-1]+nums[i])
#         res = -float('inf')
#         for i in range(len(nums)):
#             res = max(res, dp[i])
#         return res

## 滑窗
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = -float('inf')
        sum1 = 0
        while right < len(nums):
            c = nums[right]
            sum1 += c
            right += 1
            res = max(res, sum1)

            ## if shrink
            while sum1 < 0:
                sum1 -= nums[left]
                left += 1
        return res