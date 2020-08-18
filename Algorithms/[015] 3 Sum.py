# solution
# keys: 排序，去重

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # special cases
        if not nums or len(nums)<3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                return res

            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = len(nums)-1
            while L<R:
                s = nums[i]+nums[L]+nums[R]
                if s == 0:
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L] == nums[L+1]:
                        L += 1
                    while L<R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif s>0:
                    R -= 1
                else:
                    L += 1
        return res
