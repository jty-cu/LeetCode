'''
10 = 5 * 2
因为偶数一定含有2，所以10的数量取决于有多少5
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        divisor = 5
        res = 0
        while n >= divisor:
            res += n // divisor
            divisor *= 5
        return res