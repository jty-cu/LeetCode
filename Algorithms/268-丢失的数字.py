## solution 01: 位运算
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        ## 先补全索引
        res ^= n
        for i in range(n):
            res ^= i ^ nums[i]
        return res

## solution 02: 等差数列求和
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum0 = 0
        for x in nums:
            sum0 += x
        n = len(nums)
        sum1 = n*(n+1)//2
        return sum1-sum0

