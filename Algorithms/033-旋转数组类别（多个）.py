## 033、081、153、154
## 033
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0 if nums[0]==target else -1
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: ## 左侧有序，注意这里是<=, < 会有测试用例不通过
                if nums[left]<=target and target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: ## 右侧有序
                if nums[mid]<target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

## 081
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        right = n-1
        while right >= 0 and nums[right] == nums[0]:
            right -= 1
        left = 0
        if right == -1:
            return True if target==nums[0] else False
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[left] <= nums[mid]: ## 左侧有序
                if nums[left]<=target and target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

## 153
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            if nums[left] <= nums[right]:  ## 此时数组没有被翻转
                return nums[left]
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid  ##注意，mid可能是最小值

## 154
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        right = n-1
        while right>=0 and nums[right]==nums[0]:
            right -= 1
        if right == -1:
            return nums[0]
        left = 0
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left+(right-left)//2
            if nums[left]<=nums[mid]:
                left = mid + 1
            else:
                right = mid