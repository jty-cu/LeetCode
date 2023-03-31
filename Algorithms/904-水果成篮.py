'''
问题转化：最长子串问题，子串只包含两种元素
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        left, right = 0, 0
        window = dict()
        vaild = 0
        res = 0
        while right < len(fruits):
            c = fruits[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
                vaild += 1

            while vaild > 2:
                d = fruits[left]
                left += 1
                if window[d] == 1:
                    vaild -= 1
                    window.pop(d)  ## 需要把字典进行pop操作，如果window[d] = 0, right增加时不会记录valid+1而是直接更新window[d]
                else:
                    window[d] -= 1
            res = max(res, right - left)
        return res


