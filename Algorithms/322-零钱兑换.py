
## DP
'''
自顶向下的方法
用memo避免重复子问题
memo的读取和写入！！
「备忘录」大大减小了子问题数目，完全消除了子问题的冗余，所以子问题总数不会超过金额数 n，即子问题数目为 O(n)。
处理一个子问题的时间不变，仍是 O(k)，所以总的时间复杂度是 O(kn)。
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-9]*(amount+1)
        def dp(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if memo[amount] != -9:
                return memo[amount]
            ans = float('inf')
            for coin in coins:
                sub_problem = dp(coins, amount-coin)
                if sub_problem == -1:
                    continue
                ans = min(ans, sub_problem+1)
            ## 把结果存放进memo
            memo[amount] = -1 if ans==float('inf') else ans
            return ans if ans != float('inf') else -1
        return dp(coins, amount)

'''
自底向上
初始化为amount + 1
**为啥不直接初始化为 int 型的最大值 Integer.MAX_VALUE 呢？因为后面有 dp[i - coin] + 1，这就会导致整型溢出。**
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## dp定义：amount==i是=时，至少需要用dp[i]枚硬币
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i-coin < 0: ## 注意是< or <=
                    continue ## 此时该子问题无解
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[-1]==amount+1 else dp[-1]