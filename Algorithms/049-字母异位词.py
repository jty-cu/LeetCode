'''
找到一个方法，把字符出现次数相同的str打上同一个标记
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ## 记录每一个字符出现的次数
        def encode(s):
            count = [0 for _ in range(26)]
            for char in s:
                delta = ord(char) - ord('a')
                count[delta] += 1
            return str(count)

        group = dict()
        for s in strs:
            tmp = encode(s)
            if tmp in group:
                group[tmp].append(s)
            else:
                group[tmp] = [s]
        res = list()
        for x in group.values():
            res.append(x)
        return res
