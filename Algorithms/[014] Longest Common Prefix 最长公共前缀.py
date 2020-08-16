# 最长公共前缀不会超过最短的字符串

# solution 1 (excellent!)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ""
        if len(strs) == 0:
            return ""
        
        for each in zip(*strs):
            if len(set(each)) == 1: # len == 1, 说明每个str在这个位置的元素相同
                common += each[0]
            else:
                return common
        return common
        

# solution 2 (regular)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minl = min([len(x) for x in strs])
        end = 0
        
        while end < minl:
            for i in range(1,len(strs)):
                if strs[i][end]!= strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]
        
