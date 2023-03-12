'''
自顶向下的递归
'''
# class Solution:
#     ## 解决重叠子问题，防止重复计算，建立备忘录
#     def dp(self, memo, n):
#         if n == 0 or n == 1:
#             return n
#         if memo[n] != 0:
#             return memo[n]
#         return self.dp(memo, n-1) + self.dp(memo, n-2)

#     def fib(self, n: int) -> int:
#         memo = [0]*(n+1)
#         return self.dp(memo, n)

'''
自底向上的递推
'''
## 更方便的写法
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

'''
根据斐波那契数列的状态转移方程，当前状态只和之前的两个状态有关，其实并不需要那么长的一个 DP table 来存储所有的状态，只要想办法存储之前的两个状态就行了。
所以，可以进一步优化，把空间复杂度降为 O(1)。
'''