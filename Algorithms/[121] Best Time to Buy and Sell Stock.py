# solution 1 (不太聪明的亚子)
# 对于当前元素 找到后面元素中的max然后作差

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        if n == 0 or n == 1:
            return 0
        
        locmax = 0
        glomax = 0
        
        for i in range(n-1):
            tmp = max(prices[i:])
            locmax = max(locmax, tmp-prices[i])
            glomax = max(glomax,locmax)
            
        return glomax
        
        
# solution 2 (Better)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        if n == 0:
            return 0
        
        minp = prices[0]
        maxp = 0

        for i in range(1,n):
            minp = min(prices[i],minp)
            res = prices[i] - minp
            maxp = max(maxp, res)
        return maxp
