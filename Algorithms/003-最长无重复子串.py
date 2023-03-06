## 题目类型：数组
'''
2023-02-15
双指针
**1. 注意左指针更新的位置，需要直接移动到出现重复字符的地方
**2. 接1，同步关注lookup删除字符，需要删到左指针的位置
**3. cur_len的计数逻辑
'''

## 滑窗
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()
        left, right = 0, 0
        ans = 0
        while right < len(s):
            c = s[right]
            right += 1
            ## 更新window
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            ## if shrink
            while window[c] > 1:
                d = s[left]
                left += 1
                ## update window
                window[d] -= 1
            ans = max(ans, right - left)

        return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        max_len, cur_len = 0, 0
        for i in range(len(s)): ## i is right pointer
            cur_len += 1
            ## KEY: while
            while s[i] in lookup: ## 一旦出现重复的，就需要更新left pointer，删除left之前所有的字符
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(cur_len, max_len)
            lookup.add(s[i])

        return max_len