## 方法1：双指针，一前一后
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start, end = 0, n-1
        p = 0
        while p <= end:
            while p<=end and nums[p] == 2: ## 注意
                nums[end], nums[p] = nums[p], nums[end]
                end -= 1
            if nums[p] == 0:
                nums[start], nums[p] = nums[p], nums[start]
                start += 1
            p += 1
        return nums

## 方法2：使用两次双指针，先把0归位然后把1归位，2自动归位
        # left, right = 0, 0
        # while right < n:
        #     if nums[right] == 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #     right += 1
        # right = left
        # while right < n:
        #     if nums[right] == 1:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #     right += 1
        # return nums

