# solution 1
#暴力解题，遍历所有的子串: time complexity O(n^2) 

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
