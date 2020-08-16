# solution 
# 排序+双指针
# 时间复杂度：O(nlogn)+O(n^2) = O(n^2)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        ans = nums[0] + nums[1] +nums[2]
        
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            
            while start < end:
                total = nums[i] + nums[start] + nums[end]

                if abs(total-target) < abs(ans-target):
                    ans = total

                if total > target:
                    end -= 1
                elif total < target:
                    start += 1
                else:
                    return ans
        return ans
