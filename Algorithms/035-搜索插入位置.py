'''
区间类型：[, ]
更新：left=mid-1 --> [0, mid-1]; right=mid+1 [mid+1, n-1]
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

'''
区间类型：[, )
更新：left=mid --> [0, mid); right=mid+1 [mid+1, n)
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
返回该题