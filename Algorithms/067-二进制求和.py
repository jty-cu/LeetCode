'''
思路类似于445， 翻转+求和，这里是二进制
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        m, n = len(a), len(b)
        carry = 0
        i = 0
        res = list()
        while i < max(m, n) or carry > 0:
            val = carry
            if i < m:
                val += int(a[i])
            if i < n:
                val += int(b[i])
            carry, val = divmod(val, 2)
            res.append(str(val))
            i += 1 ## 别忘记+1
        return "".join(res[::-1])