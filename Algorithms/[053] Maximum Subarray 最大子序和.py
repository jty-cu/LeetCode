# solution 1 动态规划
# time complexity: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        submax = nums[0]
        glomax = nums[0]

        for i in range(1,n):
            submax = max(submax+nums[i],nums[i])
            glomax = max(submax,glomax)

        return glomax
        
# 等价方法

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        submax = 0
        glomax = nums[0]

        for i in range(n):
            submax += nums[i]
            glomax = max(submax,glomax)

            if submax < 0:
                submax = 0

        return glomax

