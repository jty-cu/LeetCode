## 考虑正负电子相抵消，多的电子决定整体的带电性
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]
        target = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count = 1
            elif nums[i] != target:
                count -= 1
            else:
                count += 1
        return target

