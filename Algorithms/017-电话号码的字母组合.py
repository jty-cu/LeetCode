## 组合问题，同077
## 注意问题转换

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = list()
        track = list()
        n = len(digits)
        if n == 0:
            return res
        used = [0 for _ in range(n)]
        def backtrack(digits, mapping, start, track):
            nonlocal res
            if len(track) == n:
                res.append("".join(track))
            for i in range(start, n):
                digit = int(digits[i])
                for j in mapping[digit]:
                    track.append(j)
                    backtrack(digits, mapping, i+1, track)
                    track.pop()
        backtrack(digits, mapping, 0, track)
        return res
