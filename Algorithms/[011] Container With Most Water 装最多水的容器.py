# solution 
# 双指针
# 时间复杂度：O(n)，空间复杂度：O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:

        i1,i2 = 0,len(height)-1
        maxsquare = 0

        while i1<i2:
            maxsquare = max( maxsquare, min(height[i1],height[i2])*(i2-i1) )

            if height[i1]<height[i2]:
                i1 += 1
            else:
                i2 -= 1

        return maxsquare
