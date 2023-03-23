class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = list()
        for i in range(n-2):
            ## 剪枝 + 去重
            if nums[i] > 0:
                return res
            if i > 0 and nums[i]  == nums[i-1]:
                continue
            ## 2sum
            target = 0-nums[i]
            low = i+1 # 注意下标
            high = n-1
            while low < high:
                sum0 = nums[low] + nums[high]
                if sum0 == target:
                    res.append([nums[i], nums[low], nums[high]])
                    while (low < high and nums[low] == nums[low+1]):
                        low += 1
                    while (low < high and nums[high] == nums[high-1]):
                        high -= 1
                    low += 1
                    high -= 1
                elif sum0 < target:
                    low += 1
                else:
                    high -= 1
        return res
