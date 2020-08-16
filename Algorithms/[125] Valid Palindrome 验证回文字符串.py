# solution
# str.isalnum 函数

class Solution:
    def isPalindrome(self, s: str) -> bool:

        seq = ''.join(filter(str.isalnum, s.lower()))
        return seq == seq[::-1]
