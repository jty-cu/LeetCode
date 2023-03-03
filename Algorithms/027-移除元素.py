## 数组；快慢指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        fast, slow = 0, 0
        while fast < len(nums):
            if (nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow ## 注意slow的计算方式，防止return错