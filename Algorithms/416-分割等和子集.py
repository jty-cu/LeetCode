## 转化成为背包问题

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums) // 2  ## 用//2来取整，如果用/2会产生float
        ## dp[i][j]=x, i:前i个物品(nums), j:背包容量(total), x:bool变量，表示是否存在一种组合可以把背包装满
        m = len(nums)
        n = total
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        ## base case
        ## dp[i][0] = True, dp[0][j] = False
        for i in range(m + 1):
            dp[i][0] = True

            ## digui
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ## 先判断 i 能不能放进背包
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:  # s1: nums[i]不放进背包, s2: nums[i]放进背包, 返回前i-1个物品和j-nums[i-1]的背包的结果
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]
'''
压缩维度
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        total = sum(nums)//2 ## 用//2来取整，如果用/2会产生float
        ## dp[i][j]=x, i:前i个物品(nums), j:背包容量(total), x:bool变量，表示是否存在一种组合可以把背包装满
        m = len(nums)
        n = total
        ## squeeze dims
        ## 思考：需要压缩的是哪一个维度
        ## 注意到 dp[i][j] 都是通过上一行 dp[i-1][..] 转移过来的，之前的数据都不会再使用了
        dp = [False for _ in range(n+1)]
        ## base case
        dp[0] = True
        for i in range(len(nums)):
            for j in range(total, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i]]
                ## 否则dp[j]的状态不变，因为物品i放不进去，还是只能在前i-1个物品中判断
                # else:
                #     dp[j] = dp[j]
        return dp[-1]