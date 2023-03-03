## 数组；快慢指针
'''
注意快慢指针是怎么使用的
快慢指针进行赋值操作时， index变换的顺序
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                ## 注意顺序
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1
