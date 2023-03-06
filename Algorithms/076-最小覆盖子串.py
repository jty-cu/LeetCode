## 数组；滑动窗口

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # from collections import defaultdict
        # need, window = defaultdict(int), defaultdict(int)
        # for c in t:
        #     need[c] += 1
        ## initial
        window, need = dict(), dict()
        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        left, right = 0, 0
        valid = 0  ## 满足要求的字符数
        start = 0  ## 记录当前最小子串的起始索引
        ans = float('inf')

        while (right < len(s)):
            ## 窗口加入字符，如何更新()
            c = s[right]
            right += 1
            if c in need:
                # 在window中进行计数
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                # 判断window是否符合need的条件
                if window[c] == need[c]: valid += 1

            ## 判断左侧窗口是否要收缩
            while valid == len(need):
                if right - left < ans:
                    start = left
                    ans = right - left
                    ## 收缩左窗口
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if ans == float('inf') else s[start:start + ans]