# solution
# Dynamic programming f(x) = f(x-1) + f(x-2)
# Fibonacci sequence
# 保存了每一步的数据

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if not n or n==1:
            return 1
        
        mem = [1,1]
        i = 2
        while i <= n:
            tmp = mem[-1]+mem[-2]
            mem.append(tmp)
            i += 1
            
        return mem[-1]
        
# 双指针
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if not n or n==1:
            return 1
        
        fir = 1
        sec = 1

        for i in range(2,n+1):
            res = fir + sec
            sec,fir = res,sec
        
        return res
            
