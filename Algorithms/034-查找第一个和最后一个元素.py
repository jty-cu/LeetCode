class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def findLeft(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:  ## 收缩右侧边界
                    right = mid - 1
            if left == n:
                return -1
            return left if nums[left] == target else -1

        def findRight(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right == n:
                return -1
            return right if nums[right] == target else -1

        p1, p2 = findLeft(nums, target), findRight(nums, target)
        return [p1, p2]