class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ["" for i in range(numRows)]
        n = len(s)
        if numRows < 2:
            return s
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -1*flag
            i += flag
        return "".join(res)