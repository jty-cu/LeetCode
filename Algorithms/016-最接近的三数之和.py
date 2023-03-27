class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        n = len(nums)
        for i in range(n-2):
            low, high = i+1, n-1
            left, right = nums[low], nums[high]
            while low < high:
                sum0 = nums[low]+nums[high]+nums[i]
                if abs(res-target) > abs(sum0-target):
                    res = sum0
                if sum0 < target:
                    low += 1
                else:
                    high -= 1
        return res