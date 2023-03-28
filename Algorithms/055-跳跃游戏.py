'''
问题转化：最远到达的距离是否 >= n-1
贪心算法，每一步都求解最优解并且和全局最优解做对比
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums)-1):
            far = max(far, i+nums[i])
            if far <= i:
                return False
        return far >= len(nums)-1
