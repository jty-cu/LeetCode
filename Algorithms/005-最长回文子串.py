## Dynamic Programming
## 中心扩展法
"""
2022-02-15
"""

## 中心扩展法
## time complexity: O(n^2)【一次遍历+每一个中心最多向外扩展O(n)次】, space complexity:O(1)
'''
1. 状态转移方程：
p(i, i) = true
p(i, i+1) = s[i] == s[i+1]
p(i, j) == p(i+1, j-1) and s[i] == s[j] (expend!)
2. 扩展的left, right的边界值
'''
class Solution:
    def expend_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:  ## 满足条件-->符合回文-->向外扩展
            left -= 1
            right += 1
        return left + 1, right - 1  ## 停止扩展，恢复到最后的回文串

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start, end = 0, 0
        ## 两种情况：1.中心为1个字符；2.中心为2个字符
        ## 遍历，比较左右指针的长度，更新左右指针
        for i in range(len(s)):
            left1, right1 = self.expend_center(s, i, i)
            left2, right2 = self.expend_center(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start: end + 1]



## 暴力解题，遍历所有的子串: time complexity O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ""
        
        length = list(range(len(s)))
        length = length[::-1]
        
        for n in length:
            for j in range(len(s)-n):
                tmp1 = s[j:j+n+1]
                tmp2 = tmp1[::-1]
                if tmp1 == tmp2:
                    return tmp1
