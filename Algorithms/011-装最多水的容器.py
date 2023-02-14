## 问题类型：数组
'''
2023-02-14
双指针
时间复杂度：O(n)，空间复杂度：O(1)
**1. S = min(height[i], height[j]) * abs(i-j)
**2. 指针移动：短板内移

'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1 ## gap = j-i
        ans = 0
        while i < j:
            cur = min(height[i], height[j])*(j - i)
            ans = max(ans, cur)
            if height[i] <= height[j]: ## 指针移动：谁短谁动
                i += 1
            else:
                j -= 1
        return ans
