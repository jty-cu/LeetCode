## 在题目描述中出现了 nums[-1] = nums[n] = -∞，这就代表着 只要数组中存在一个元素比相邻元素大，那么沿着它一定可以找到一个峰值
## 往递增的方向上，二分，一定能找到，往递减的方向只是可能找到，也许没有。
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = left + (right-left) // 2
            ## 往递增方向走
            if nums[mid] <= nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left