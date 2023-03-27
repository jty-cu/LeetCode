'''
1. 识别到最短的单词
2. 遍历strs中的所有单词，按照最短单词中的字符顺序进行判断，一旦有不符合的立刻返回res(剪枝)
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## find shortest word
        shortIdx = -1
        shortLen = float('inf')
        res = list()
        for i in range(len(strs)):
            if len(strs[i]) < shortLen:
                shortLen = len(strs[i])
                shortIdx = i
        shortStr = strs[shortIdx]

        for i in range(shortLen):
            for str0 in strs:
                if str0[i] != shortStr[i]:
                    return "".join(res)
            res.append(shortStr[i])
        return "".join(res)